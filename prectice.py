print("--------- HOSPITAL MANAGEMENT SYSTEM ----------\n")
patients = {}


def add_patient():
    try:
        pid = int(input("Please enter patient ID: "))
        if pid in patients:
            print(f"ID: {pid} already exists please choose another ID !!")
            return
        
        name = input("Please enter patient name: ")
        age = int(input("Please enter patient age: "))
        disease = input("Enter the patient disease: ")

        patients[pid] = {
            "name": name,
            "age": age,
            "disease": disease,
        }

        print("Patient Added successfully !!")
    except Exception as e:
        print(f"Error: {e}")

def view_patient():
    print("\n--------- All Patient Here ---------")
    print("Total Patients: ",len(patients))
    for pid,details in patients.items():
        print(f"ID: {pid} || Name: {details['name']} || Age: {details['age']} || Disease: {details['disease']}")
    
    
def search_patient():
    try:
        pid = int(input("Please enter patient ID: "))

        if pid not in patients:
            print(f"ID: {pid} Patient not exists !!")
            return
        else:
            print("\n-------- Search Patient Here ----------")
            print(f"ID: {pid} || Name: {patients[pid]['name']} || Age: {patients[pid]['age']} || Disease: {patients[pid]['disease']}")
    except Exception as e:
        print(f"Error: {e}")

def delete_patient():
    try:
        pid = int(input("Please enter the patient ID: "))

        if pid in patients:
            print(f"ID: {pid} || Name: {patients[pid]['name']} || Age: {patients[pid]['age']} || Disease: {patients[pid]['disease']}")
            del patients[pid]
            print("\n--------- Patient Deleted successfully ---------")
            return
        else:
            print(f"ID: {pid} Patient not exists !!")
    except Exception as e:
        print(f"Error: {e}") 
while True:
    print("\n======== HOSPITAL MANAGEMENT SYSTEM =========")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice==1:
            add_patient()
        elif choice==2:
            view_patient()
        elif choice==3:
            search_patient()
        elif choice==4:
            delete_patient()
        elif choice==5:
            print("Thanks to use my hospital management project to use your resume !! Exit..")
            break
        else:
            print("Invalid choice !! try again...")
    except Exception as e:
        print(f"Error: Please enter a valid number !!")