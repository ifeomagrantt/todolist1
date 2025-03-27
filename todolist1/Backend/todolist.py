import json       # For storing tasks in a JSON file
import argparse   # For handling command-line arguments
from datetime import datetime  # For timestamps

TASK_FILE = "tasks.json"

parser = argparse.ArgumentParser("todo")
parser.add_argument("-a", "--add", help="Add a new task", type=str)
parser.add_argument("-d", "--delete", help="delete a task", type=int)
parser.add_argument("-u","--update", help = "update status", type=str)
parser.add_argument("--id", help = "retrieve id", type=int)
parser.add_argument("--tasks", help = "print tasks", action="store_true")
parser.add_argument("--incomplete_tasks", help = "print incomplete tasks", action="store_true")
parser.add_argument("--inprogress_task", help = "print inprogress tasks", action="store_true")

args = parser.parse_args()


def load_tasks():
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def  add_task(description):
    tasks = load_tasks()
    uniqueID = max([task["id"] for task in tasks], default=0) + 1

    new_task = {
        "id": uniqueID,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%I:%M %p %m/%d/%y"),
        "updatedAt": datetime.now().strftime("%I:%M %p %m/%d/%y")
    }
    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {uniqueID})")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(updated_tasks):  # No change means ID was not found
        print(f"Task with ID {task_id} not found!")
        return

    save_tasks(updated_tasks)
    print(f"Task with ID {task_id} deleted successfully!")


def update_status(status, task_id =None):
    tasks = load_tasks()

    if task_id is None:
        task_id = args.id

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status.lower()
            task["update"] = datetime.now().strftime("%I:%M %p %m/%d/%y")
            save_tasks(tasks)
            break

def print_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(task)

def print_incomplete_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] != "completed":
            print(task)

def print_in_progress_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "in-progress".lower():
            print(task)
"""



"""

if args.add:
    add_task(args.add)


if args.delete:
    delete_task(args.delete)

if args.update:
    update_status(args.update)

if args.tasks:
    print_tasks()

if args.incomplete_tasks:
    print_incomplete_tasks()

if args.inprogress_task:
   print_in_progress_tasks()