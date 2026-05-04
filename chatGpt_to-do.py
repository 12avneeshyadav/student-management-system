import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file ------------------------------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file ---------------------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Display all tasks ----------------------------------------
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    print("\n--- All Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["completed"] else "⏳ Pending"
        print(f"{i}. {task['title']}  --> {status}")
    print()

# Add new task ---------------------------------------------
def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Task cannot be empty.\n")

# Mark task as completed ------------------------------------
def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to complete: "))
        tasks[num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!\n")
    except:
        print("Invalid input.\n")

# Delete task -----------------------------------------------
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted!\n")
    except:
        print("Invalid input.\n")

# Main Program ----------------------------------------------
def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO MENU ====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
