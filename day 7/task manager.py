import datetime

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

def check_positive_negative(number):
    if number > 0:
        return f"{number} is Positive"
    elif number < 0:
        return f"{number} is Negative"
    else:
        return f"{number} is Zero"

def display_menu():
    print("\nBasic Python Program:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Check if a number is even or odd")
    print("6. Check if a number is positive, negative, or zero")
    print("7. Exit")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {add(a, b)}")

        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {subtract(a, b)}")

        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {multiply(a, b)}")

        elif choice == "4":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {divide(a, b)}")

        elif choice == "5":
            number = int(input("Enter a number: "))
            print(check_even_odd(number))

        elif choice == "6":
            number = float(input("Enter a number: "))
            print(check_positive_negative(number))

        elif choice == "7":
            print("\nExiting the program. Goodbye!\n")
            break

        else:
            print("\nInvalid choice. Please try again.\n")
