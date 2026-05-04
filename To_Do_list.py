print("\n<===============TO-DO List created by AVNEESH YADAV==============>")

tasks = []

def add_task():
    print("\n------------Added Your Task-----------------")
    count = int(input("Enter the task No: "))
    
    for eachTask in tasks:
        if eachTask['count'] == count:
            print("This Task already Exists !!")
            return
    task_no = input("Enter your newtask:")
    task = {
        "count": count,
        "task" : task_no
    }
    tasks.append(task)
    print("\n--------------Task Added Successfully----------------")


def view_task():
    print("\n--------------View All Tasks----------------")
    if len(tasks) == 0:
        print("Task Not Available !!")
    for eachTask in tasks:
        print(f"Task No {eachTask['count']}--> {eachTask['task']}")
        

def complete_task():
    view_task()
    print("\n--------------Complete Task-----------------")
    choices = int(input("Enter the task no: "))
    for eachTask in tasks:
        if eachTask['count'] == choices:
            print(f"{eachTask['task']} Completed !!")

def delete_task():
    view_task()
    if len(tasks)== 0:
        print("Task not Available !!")
    
    count = int(input("Enter the task no, you want to delete: "))
    for eachTask in tasks:
        if eachTask['count'] == count:
            tasks.remove(eachTask)
    
    print("\n-------------Task Deleted Successfully-----------------")
        
        

    
    

while True:
    print("\n<===============Main Menu===============>")
    print("1. Add Tasks")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = int(input("Enter Your choice: "))
    
    if choice == 1:
        add_task()
    
    elif choice == 2:
        view_task()

    elif choice == 3:
        complete_task()
    
    elif choice == 4:
        delete_task()
    
    elif choice == 5:
        break
    
    else:
        print("Invalid choice by User !!")