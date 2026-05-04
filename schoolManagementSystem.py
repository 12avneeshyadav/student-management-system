# today i create a new project student management system using python---------->  Date-> 2025|11|29

print("<============STUDENT MANAGEMENT SYSTEM created by AVNEESH YADAV=============>")

students = []

def add_student():
    print("\n----------Add Student-----------")
    roll = int(input("Enter Roll Number: "))
    
    for s in students:
        if s["roll"] == roll:
            print("This Student Already Exists !!")
            return
    
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    
    student = {
        "roll" : roll,
        "name" : name,
        "marks" : marks, 
    }
    
    students.append(student)
    
    print("\n---------Student Added Successfully---------")
    
def display_student():
    print("\n-----------Display All Student-----------")
    if len(students) == 0:
        print("Student not Available !!")
        return
    
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
    

def search_student():
    print("\n----------Search Student by Roll Number-----------")
    roll = int(input("Enter Roll Number: "))
    
    for s in students:
        if s["roll"] == roll:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
            return
        
    print("Student Not Found !!")
    
def update_marks():
    print("\n-----------Update Student Marks------------")
    roll = int(input("Enter Roll Number: "))
    
    for s in students:
        if s["roll"] == roll:
            new_marks = int(input("Enter New Marks: "))
            s["marks"] = new_marks
            print("Marks Updated Successfully !!")
            return
        
    print("Student Not Found !!")


def delete_student():
    print("\n---------Delete A Student---------")
    
    roll = int(input("Enter Roll Number: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            
            print("Student Deleted Successfully !!")
            return
        
    print("Student Not Found !!")
    

def show_topper():
    print("\n-----------Topper------------")
    
    if len(students) == 0:
        print("Student Not Available !!")
        return
    
    topper = max(students, key=lambda x: x["marks"])
    
    print(f"Roll: {topper['roll']}, Name: {topper['name']}, Marks: {topper['marks']}")


while True:
    print("<================Main Menu================>")
    
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Search Student by Roll No.")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")
    
    choice = int(input("Enter Your choice: "))
    
    if choice == 1:
        add_student()
    
    elif choice == 2:
        display_student()
    
    elif choice == 3:
        search_student()
    
    elif choice == 4:
        update_marks()
    
    elif choice == 5:
        delete_student()
    
    elif choice == 6:
        show_topper()
    
    elif choice == 7:
        print("Exit, Thanks !!")
        break
    
    else:
        print("Invalid Choice !!")