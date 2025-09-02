
# Command-Line Task Tracker

A simple, command-line based task management tool built with Python. This script allows you to add, list, update, delete, and change the status of your tasks directly from the terminal.

All tasks are stored locally in a `tasks.json` file.

---

## Features

-   **Add Tasks**: Add new tasks to your list.
-   **List Tasks**: View all tasks or filter them by status (`todo`, `in-progress`, `done`).
-   **Update Tasks**: Modify the description of an existing task.
-   **Delete Tasks**: Remove a task from your list.
-   **Update Status**: Mark tasks as "in-progress" or "done".

---

## Prerequisites

-   Python 3

---

## Usage

No installation is needed. Run the script directly using `python3`.

### General Help
To see the list of available commands:
```bash
python3 task_tracker.py
```

### Add a Task
```bash
python3 task_tracker.py add "Your new task description here"
```

### List Tasks
-   **List all tasks:**
    ```bash
    python3 task_tracker.py list
    ```
-   **List tasks by status:**
    ```bash
    python3 task_tracker.py list todo
    python3 task_tracker.py list in-progress
    python3 task_tracker.py list done
    ```

### Update a Task
You need to provide the task's ID and the new description.
```bash
python3 task_tracker.py update <task_id> "The updated task description"
```
*Example:*
```bash
python3 task_tracker.py update 1 "A better description for my first task"
```

### Delete a Task
```bash
python3 task_tracker.py delete <task_id>
```
*Example:*
```bash
python3 task_tracker.py delete 2
```

### Mark a Task's Status
-   **Mark as "In Progress":**
    ```bash
    python3 task_tracker.py mark-in-progress <task_id>
    ```
-   **Mark as "Done":**
    ```bash
    python3 task_tracker.py mark-done <task_id>
    ```

---

## Data Storage

This tool creates and uses a `tasks.json` file in the same directory where the script is run. This file stores all your task objects.

### Task Schema
Each task is a JSON object with the following structure:
```json
{
    "id": 1,
    "description": "This is a sample task",
    "status": "todo",
    "createdAt": "2023-10-27T10:00:00.000000",
    "updatedAt": "2023-10-27T10:00:00.000000"
}