print("================ Cafe Management System =============\n")

menu = {
    # Fast Food
    "Burger": 120,
    "Cheese Burger": 150,
    "Veg Sandwich": 90,
    "Grilled Sandwich": 130,
    "French Fries": 80,
    "Peri Peri Fries": 100,
    "Pizza": 200,

    # Snacks
    "Samosa": 20,
    "Kachori": 25,
    "Patties": 35,
    "Garlic Bread": 90,
    "Nachos": 140,

    # Beverages
    "Tea": 50,
    "Green Tea": 60,
    "Black Coffee": 90,
    "Cold Coffee": 130,
    "Cappuccino": 150,
    "Latte": 160,
    
}

order = {}

def show_menu():
    print("\n-------- Cafe Menu --------")
    for item, price in menu.items():
        print(f"{item} : {price} Rs")
    
def teke_order():
    item = input("Enter item: ").title()
    
    if item in menu:
        qty = int(input("Enter quatity: "))
        
        if item in order:
            order[item] += qty
        else:
            order[item] = qty
        print("Item Added to order !!")
    else:
        print("Item not Available in menu !!")

def show_bill():
    if not order:
        print("No order placed yet !!")
        return
    
    total = 0
    print("\n----------- Bill -----------")
    for item, qty in order.items():
        price = menu[item] * qty
        print(f"{item} X {qty} = {price}")
        
        total+=price
    
    print("---------------------------")
    print(f"Total Bill: {total} Rs")


while True:
    print("\n-------------- Cafe Management Menu ----------------")
    print("1. Show Menu")
    print("2. Order Item")
    print("3. Show Bill")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        show_menu()
    elif choice == "2":
        teke_order()
    elif choice == "3":
        show_bill()
    elif choice == "4":
        break
    else:
        print("Invalid choice !! try again.")