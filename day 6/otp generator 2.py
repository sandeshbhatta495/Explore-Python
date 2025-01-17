import random

def menu():
    print("******************************")
    print("******************************")
    print("Welcome To OTP Generation App")
    print("Choose an option:")
    print("1. Want to generate code for Facebook Login.")
    print("2. Want to generate code for Google Verification.")
    print("3. Want to generate code for Other/Extra App verification.")
    print("4. Exit This Program.")
    print("******************************")

def facebook(name):
    print(f"Welcome, {name} \nIn Code Generator.")
    print("You have chosen the Facebook Code Generation.")
    code = random.randint(100000, 999999)
    print(f"Code for Facebook: {code}\n")

def google(name):
    print(f"Welcome, {name} \nIn Code Generator.")
    print("You have chosen the Google Code Generation.")
    code = random.randint(100000, 999999)
    print(f"Code for Google: {code}\n")

def other(name):
    print(f"Welcome, {name} \nIn Code Generator.")
    print("You have chosen the Other/Extra App Code Generation.")
    code = random.randint(100000, 999999)
    print(f"Code for Other Apps: {code}\n")

def main():
    while True:
        menu()
        name = input("Enter Your Name: ")

        choice = int(input("Enter Your Choice (1-4): "))

        if choice == 1:
            facebook(name)
        elif choice == 2:
            google(name)
        elif choice == 3:
            other(name)
        elif choice == 4:
            print("Exiting the Program. Thank you for using our product!")
            break
        else:
            print("Invalid choice! Please enter a valid choice (1-4).\n")

main()
