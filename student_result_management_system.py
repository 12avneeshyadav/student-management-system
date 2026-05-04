print("========== Student Result Management System =========\n")

students=[]


def calculate_percentage(percentage):
    if percentage>=75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 45:
        return "C"
    else:
        return "fail"
    
def add_student():
    roll = int(input("Enter Roll Number: "))
    for eachRoll in students:
        if eachRoll['roll'] == roll:
            print("Student Already exists !!")
            return
    
    name = input("Enter Name: ")
    m1 = int(input("Enter first subject marks: "))
    m2 = int(input("Enter second subject marks: "))
    m3 = int(input("Enter third subject marks: "))
    total = m1+m2+m3
    percentage = total/3
    grade = calculate_percentage(percentage)
    student = {
        "roll": roll,
        "name": name,
        "marks": [m1, m2, m3],
        "total": total,
        "percentage": percentage,
        "grade": grade
    }
    
    students.append(student)
    
    print("========= Student Added Successfully ==========\n")

def show_student():
    print("\n========== All Students =============")
    if not students:
        print("No studnt record found !!\n")
        return
    for eachStudnt in students:
        print(f"Roll no: {eachStudnt['roll']}")
        print(f"Name: {eachStudnt['name']}")
        print(f"Marks: {eachStudnt['marks']}")
        print(f"Total: {eachStudnt['total']}")
        print(f"Percentage: {eachStudnt['percentage']}")
        print(f"Grade: {eachStudnt['grade']}")
        print("\n----------------------------------\n")

def search_student():
    print("\n----------- Search Student by roll no -----------\n")
    roll = int(input("Enter roll no: "))
    if not students:
        print("No studnt record found !!\n")
        return
    found = False
    
    for eachStudnt in students:
        if eachStudnt['roll'] == roll:
            print(f"Roll no: {eachStudnt['roll']}")
            print(f"Name: {eachStudnt['name']}")
            print(f"Marks: {eachStudnt['marks']}")
            print(f"Total: {eachStudnt['total']}")
            print(f"Percentage: {eachStudnt['percentage']}")
            print(f"Grade: {eachStudnt['grade']}\n")
            found = True
    if not found:
        print("Student not found !!\n")

    print("--------------------------------------\n")


while True:
    print("\n=========== Main Menu =========")
    print("1. Add Student")
    print("2. Show All Student")
    print("3. Search Student")
    print("4. Exit")
    
    try:
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            add_student()
        
        elif choice == 2:
            show_student()
        
        elif choice == 3:
            search_student()
        
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid number by the User !!")
    
    except ValueError:
        print("Error: Please enter a Valid Number !!")
        continue
    