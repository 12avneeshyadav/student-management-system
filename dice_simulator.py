
students = {}
def add_student():
    roll = int(input("Enter Roll Number: "))
    
    if roll in students:
        print("Student Already exists !!")
    
    else:
        name = input("Enter Name: ")
        
        students[roll] = {
            "name": name,
            "marks": []
        }

def add_marks():
    roll = int(input("Enter Student Roll no: "))
    
    if roll not in students:
        print("Student Not Found !!")
        return
    
    marks = int(input("Enter Marks(0-100): "))
    if 0<= marks <= 100:
        students[roll]['marks'].append(marks)
    
    else:
        print("marks must be between 0 and 100.")