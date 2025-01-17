# Pizza Ordering Program with Customization

# Take user input for the size of the pizza
choice = input("Enter the size of pizza (S/M/L): ").upper()  
bill = 0

# Pizza size prices
if choice == 'S':
    bill += 100
    print("You have chosen a small pizza with basic toppings. The price is Rs 100.")
elif choice == 'M':
    bill += 300
    print("You have chosen a medium pizza with main course toppings. The price is Rs 300.")
elif choice == 'L':
    bill += 500
    print("You have chosen a large pizza with main course toppings and a bottle of coke. The price is Rs 500.")
else:
    print("Invalid choice. Please select S, M, or L.")
    exit()  # Exit the program if the input is invalid

# Add-ons
print("\nWould you like to add any of the following extras?")
add_pepperoni = input("Do you want extra pepperoni for Rs 50? (Y/N): ").upper()
if add_pepperoni == 'Y':
    bill += 50
    print("Extra pepperoni added for Rs 50.")

add_cheese = input("Do you want extra cheese for Rs 30? (Y/N): ").upper()
if add_cheese == 'Y':
    bill += 30
    print("Extra cheese added for Rs 30.")

add_coke = input("Do you want an extra bottle of coke for Rs 40? (Y/N): ").upper()
if add_coke == 'Y':
    bill += 40
    print("Extra bottle of coke added for Rs 40.")

# Display the total bill
print(f"\nYour total bill is: Rs {bill}")

# Ask if the customer is excited about their pizza
a = input("Are you excited for your pizza? (Y/N): ").upper()
if a == 'Y':
    print("Thank you so much! We are also excited about your order.")
    print("OK, your order is ready!")
elif a == 'N':
    print("We hope you will enjoy your pizza soon!")
else:
    print("Invalid response. Please answer with Y or N.")
