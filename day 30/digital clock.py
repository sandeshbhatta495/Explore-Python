from datetime import datetime
import time

admin = "sandesh"

def menu():
    global admin
    cont = input("Are You Admin of This Program? (y/n): ").lower()
    if cont == 'y':
        password = input("Enter the admin name: ")
        if password == admin:
            print("Welcome Sir Namaste!")
            change()
        else:
            print("Incorrect admin name.")
            exit()
    else:
        exit()

def change():
    print("Admin functionality can be added here.")

def time_display():
    # Get the current date and time
    current_datetime = datetime.now()

    # Display the date and time
    print("Current Date and Time:", current_datetime)

    # Format the date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print("Formatted Date and Time:", formatted_datetime)

def clear_screen():
    print("c", end="")

if __name__ == "__main__":
    menu()
    while True:
        clear_screen()
        time_display()
        time.sleep(1)