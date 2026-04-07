# CLI Task Tracker

A simple command-line tool to manage your tasks efficiently.

(A recommended project for the Backend Developer Roadmap at https://roadmap.sh/projects/task-tracker)

## Usage

```
task-cli <command> [arguments]
```

## Commands

| Command | Arguments | Description |
|---|---|---|
| `add` | `<title>` | Add a new task |
| `update` | `<id> <title>` | Update an existing task |
| `delete` | `<id>` | Delete a task |
| `mark-in-progress` | `<id>` | Mark a task as in progress |
| `mark-done` | `<id>` | Mark a task as done |
| `list` | `[status]` | List tasks (optionally filter by status) |

## Status Values

- `todo`
- `in-progress`
- `done`

## Examples

```bash
# Add a new task
task-cli add "Buy groceries"

# Update an existing task
task-cli update 1 "Buy groceries and cook dinner"

# Delete a task
task-cli delete 1

# Mark a task as in progress
task-cli mark-in-progress 1

# Mark a task as done
task-cli mark-done 1

# List all tasks
task-cli list

# List tasks filtered by status
task-cli list done
```

## Options

| Flag | Description |
|---|---|
| `-h`, `--help` | Show this help message |
| `-v`, `--version` | Show version number |
