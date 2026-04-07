version = 0.1

import sys
import json

def print_usage():
    print()
    with open(".\\task-cli_usage.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())
    print()

def get_or_create_json():
    tasks_json = {"tasks": [], "tasks_count": 0, "next_id": 1}

    try:
        with open(".\\task_db.json", "r") as f:
            tasks_json = json.load(f)
    except FileNotFoundError:
        with open(".\\task_db.json", "w") as f:
            f.write(json.dumps(tasks_json))

    return tasks_json

def id_is_int(id):
    try:
        task_id = int(id)
    except ValueError:
        print(f"Invalid value for id: '{id}'. An integer is expected. Use -h or --help for help.")
        return False
    
    return True

def get_task_by_id(stored_tasks, task_id):
    if id_is_int(task_id):
        existing_task = [x for x in stored_tasks["tasks"] if int(x["id"]) == int(task_id)]
        
        if len(existing_task) > 0:
            return existing_task[0]
        else:
            raise ValueError(f"No task with id: {task_id}.")


def add_task(argv, stored_tasks):
    stored_tasks["tasks_count"] += 1
    stored_tasks["tasks"].append({
        "id": stored_tasks["next_id"],
        "status": "todo",
        "title": argv[1]
    })
    stored_tasks["next_id"] += 1

    return stored_tasks

def update_task(argv, stored_tasks, new_value={}):    
    if len(new_value.keys()) == 0:
        new_value = {
            "title": argv[2]
        }

    try:
        stored_task = get_task_by_id(stored_tasks, argv[1])
    
        for key in new_value.keys():
            stored_task[key] = new_value[key]
    except ValueError as ve:
        print(ve)

    return stored_tasks
    
def delete_task(argv, stored_tasks):
    try:
        stored_task = get_task_by_id(stored_tasks, argv[1])
        stored_tasks["tasks"].remove(stored_task)
        stored_tasks["tasks_count"] -= 1
    except ValueError as ve:
        print(ve)

    return stored_tasks
    
def mark_in_progress(argv, stored_tasks):
    try:
        stored_task = get_task_by_id(stored_tasks, argv[1])
        return update_task(argv, stored_tasks, {"status": "in-progress"})
    
    except ValueError as ve:
        print(ve)

def mark_done(argv, stored_tasks):
    try:
        stored_task = get_task_by_id(stored_tasks, argv[1])
        return update_task(argv, stored_tasks, {"status": "done"})
    
    except ValueError as ve:
        print(ve)

def list_tasks(argv, stored_tasks):
    to_print = []
    status = argv[1] if len(argv) > 1 else 'all'

    if status == 'all':
        to_print = stored_tasks["tasks"]
    else:
        to_print = [x for x in stored_tasks["tasks"] if x["status"] == status]
    
    print("\nID  STATUS       TITLE")
    for task in to_print:
        print(f"{str(task['id']).ljust(4, ' ')}{task['status'].ljust(12, ' ')}\t{task['title']}")
    print()

if __name__ == "__main__":
    commands_dict = {
        'add': add_task,
        'update': update_task,
        'delete': delete_task,
        'mark-in-progress': mark_in_progress,
        'mark-done': mark_done,
        'list': list_tasks
    }
    
    commands_list = list(commands_dict.keys())

    if len(sys.argv) > 1:
        command = sys.argv[1].strip().lower()

        if command in ['-h', '--help']:
            print_usage()
        elif command in ['-v', '--version']:
            print(f"task-cli version: {version}")
        elif command in commands_list:
            stored_tasks = get_or_create_json()
            try:
                stored_tasks = commands_dict[command](argv=sys.argv[1:], stored_tasks=stored_tasks)
                
                if not stored_tasks is None:
                    with open(".\\task_db.json", "w") as f:
                        f.write(json.dumps(stored_tasks))

            except IndexError:
                print_usage()
        else:
            print_usage()
    else:
        print_usage()
    