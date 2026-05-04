print("=========== ATM Simulater ===========\n")

balance = 5000

def check_balance(balance):
    print(f"Current Balance in your Account: {balance}\n")
    return balance

def deposite(balance):
    ammount = int(input("Enter the money :"))
    if ammount > 0:
        balance += ammount
        print(f"{ammount} Deposited Successfully !!\n")
        
    else:
        print(f"Invalid input !!")
    return balance

def withdraw(balance):
    ammount = int(input("Enter the money :"))
    
    if ammount > balance:
        print(f"Insufficient Balance !!\n")
        
    elif ammount <= 0:
        print("Invalid Ammount !!\n")
    
    else:
        balance -= ammount
        print(f"{ammount} Withdrawl Successfully !!\n")
        
    return balance

while True:
    print("======= Main Menu ========\n")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Choose an option (1-4): "))
    
    if choice == 1:
        balance = check_balance(balance)
    
    elif choice == 2:
        balance = deposite(balance)
    
    elif choice == 3:
        balance = withdraw(balance)
    
    elif choice == 4:
        print("Exit !! ThaknYou...")
        break
    else:
        print("Invlid Input !!")