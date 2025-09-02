"""
Psueodocde:
1. create tasks.json if it doesn't exist
2. load tasks from tasks.json
3. reads user arguments 
4. add, delete, list tasks based on user arguments
5. if add (without task_description arg) --> display usage task_tracker.py add "task description"
6. if add (with task_description arg) --> add task to tasks.json with id = len(tasks) + 1
7. if update (without task_id and _task_description args) --> display usage task_tracker.py update <task_id> "new task description"
8. if update (with required args) --> search for id and update task description
9. if delete (without task_id arg) --> display usage task_tracker.py delete <task_id>
10.if delete (with task_id arg) --> search for id and delete task
11. if list --> display all tasks in tasks.json
12. if list (with status arg) --> display tasks with that status
13. if mark-<status> (without task_id arg) --> display usage task_tracker.py mark-<status> <task_id>
14. if mark-<status> (with task_id arg) --> search for task with that id and update status accordingly.

Task object schema:
id: int
desccription: string
status: todo, done, in-progress (default is todo)
createdAt: timestamp
updatedAt: timestamp

Possible usage(s):
python3 task_tracker.py add "task description"
python3 task_tracker.py update <task_id> "new task description"
"""

import sys
import json
from datetime import datetime
import os

tasks = []

if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as f:
        json.dump([], f)

with open("tasks.json", "r") as tasks_file:
    content = tasks_file.read()
    if content.strip():
        tasks = json.loads(content)
    else:
        tasks = []

if len(sys.argv) < 2:
    print("\nUsage: python3 task_tracker.py <command> [arguments]")
    print("""
            ** Commands **
            - add 
            - list <option>: todo, in-progress, done
            - update 
            - delete 
            - mark-in-progress 
            - mark-done
          """)
    exit(0)

match sys.argv[1]:
    case "add":
        try:
            if len(sys.argv) != 3:
                print("Usage: python3 task_tracker.py add <task_description>")
                exit(0)
            else:
                tasks.append(
                    {
                        "id": len(tasks) + 1,
                        "description": sys.argv[2], 
                        "status": "todo",            
                        "createdAt": datetime.now().isoformat(),  
                        "updatedAt": datetime.now().isoformat()
                    }
                )
                print(f"Task {sys.argv[2]} with added successfully!")
                
        except Exception as e:
            print("An error occurred during adding tasks.", e)
            exit(1)

    case "list":
        try:
            if len(tasks) < 1:
                print("No tasks added yet.")
                exit(0)
            elif len(sys.argv) < 3:
                for task in tasks:
                    print(task)
                exit(0)  
            else:
                for task in tasks:
                    if task["status"] == sys.argv[2]:
                        print(task)
                exit(0)
        
        except Exception as e:
            print("An error occurred during task listing process.", e)
            exit(1)


    case "update":
        try:
            if len(sys.argv) != 4:
                print("Usage: python3 task_tracker.py update <task_id> <updated_task_description>")
                exit(0)
            else:
                update_task_id = sys.argv[2]
                updated_description = sys.argv[3]
                found = False
                for task in tasks:
                    if int(task["id"]) == int(update_task_id):
                        task["description"] = updated_description
                        task["updatedAt"] = datetime.now().isoformat()
                        found = True
                        print(f"Task with id {update_task_id} updated successfully to {updated_description}.")
                        break
                if not found:  
                    print(f"Task with id {update_task_id} not found.")
                    exit(0)

        except Exception as e:
            print("An error occurred during the task updating process.", e)
            exit(1)
    
    case "delete":
        try:
            if len(sys.argv) != 3:
                print("Usage: python3 task_tracker.py delete <task_id>")
                exit(0)
            else:
                delete_task_id = sys.argv[2]
                to_delete_found = False
                for task in tasks:
                    if int(task["id"]) == int(delete_task_id):
                        tasks.remove(task)
                        print(f"Task with id {delete_task_id} successfully deleted.")
                        to_delete_found = True
                        break
                if not to_delete_found: 
                    print(f"Task with id {delete_task_id} is not found and cannot be deleted.")
                    exit(0)

        except Exception as e:
            print("An error occurred during the deletion process.", e)
            exit(1)

    case "mark-in-progress":
        try:
            if len(sys.argv) != 3:
                print("Usage: python3 task_tracker.py mark-in-progress <task_id>")
                exit(0)
            else:
                mark_task_id = sys.argv[2]
                mark_found = False
                for task in tasks:
                    if int(task["id"]) == int(mark_task_id):
                        task["status"] = "in-progress" 
                        print(f"Task with id {mark_task_id} marked to in-progress.")
                        mark_found = True
                        break
                if not mark_found:  
                    print(f"Task with id {mark_task_id} not found.")
                    exit(0)
        except Exception as e:
            print("An error occurred during task marking.", e)
            exit(1)

    
    case "mark-done":
        try:
            if len(sys.argv) != 3:
                print("Usage: python3 task_tracker.py mark-done <task_id>")
                exit(0)
            else:
                mark_task_id = sys.argv[2]
                mark_found = False
                for task in tasks:
                    if int(task["id"]) == int(mark_task_id):
                        task["status"] = "done"  
                        print(f"Task with id {mark_task_id} marked to done.")
                        mark_found = True
                        break
                if not mark_found:
                    print(f"Task with id {mark_task_id} not found.")
                    exit(0)
        except Exception as e:
            print("An error occurred during task marking.", e)
            exit(1)
            
            
with open("tasks.json", "w") as tasks_file:
    json.dump(tasks, tasks_file, indent=4)
    
exit(0)