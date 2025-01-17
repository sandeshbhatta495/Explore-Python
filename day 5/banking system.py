def menu():
    print("******************************")
    print("Banking Program")
    print("******************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("******************************")


def withdraw():
    global money
    global name
    print("Welcome to the withdrawal portal:")
    amount = float(input("Enter the amount you want to withdraw: "))
    if 0 < amount <= money:
        money -= amount
        print
money = 0
name=input("Enter your name :")

def show_balance():
    global money
    global name
    print(f"Your balance in your account: Rs {money:.2f}")

def deposit():
    global money
    global name
    print("Welcome to the deposit portal:")
    amount = float(input("Enter the amount you want to deposit: "))
    if amount > 0:
        money += amount
        print(f"Successfully deposited Rs {amount:.2f}. New balance: Rs {money:.2f}")
        print(f"Hello, {name}, you have deposited an amount into your account.")
        print(f"Your final balance is Rs {money:.2f}.")
        print("Thank you for visiting our bank.")
    else:
        print("Invalid amount. Please try again.")
while True:
    menu()
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            show_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    print("\n")
