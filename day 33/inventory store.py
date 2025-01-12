import pandas as pd
import csv

def load_products(file_name='products.csv'):
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        print("Error: File not found!")
        return pd.DataFrame()


def display_products(products):
    print("\nAvailable Products:")
    print(products[['ProductID', 'ProductName', 'Category', 'Price', 'Stock']])


def search_product(products, name):
    result = products[products['ProductName'].str.contains(name, case=False)]
    return result if not result.empty else "No matching product found!"


def add_to_cart(products, cart, product_id, quantity):
    product_row = products[products['ProductID'] == product_id]
    if not product_row.empty:
        stock = product_row.iloc[0]['Stock']
        if quantity <= stock:
            product_name = product_row.iloc[0]['ProductName']
            price = product_row.iloc[0]['Price']
            cart.append((product_id, product_name, quantity, price))
            products.loc[products['ProductID'] == product_id, 'Stock'] -= quantity
            print(f"Added {quantity} of {product_name} to the cart.")
        else:
            print(f"Insufficient stock! Only {stock} available.")
    else:
        print("Invalid Product ID.")

# Calculate total cost of the cart
def calculate_total(cart):
    total = sum(item[2] * item[3] for item in cart)
    return total

# Save the invoice to a CSV file
def save_invoice(cart, file_name='invoice.csv'):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ProductID', 'ProductName', 'Quantity', 'Price', 'Total'])
        for item in cart:
            writer.writerow([item[0], item[1], item[2], item[3], item[2] * item[3]])
        writer.writerow([])
        writer.writerow(['Total Amount', '', '', '', calculate_total(cart)])
    print(f"Invoice saved to {file_name}")

# Main store system
def store_management_system():
    products = load_products()
    if products.empty:
        return

    cart = []
    while True:
        print("\nStore Management System:")
        print("1. View Products")
        print("2. Search Product")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Checkout and Save Invoice")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_products(products)
        elif choice == '2':
            search_name = input("Enter product name to search: ")
            print(search_product(products, search_name))
        elif choice == '3':
            try:
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))
                add_to_cart(products, cart, product_id, quantity)
            except ValueError:
                print("Invalid input! Please enter numeric values for Product ID and Quantity.")
        elif choice == '4':
            if cart:
                print("\nCart Items:")
                for item in cart:
                    print(f"ProductID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: ${item[3]}, Total: ${item[2] * item[3]}")
            else:
                print("Your cart is empty.")
        elif choice == '5':
            if cart:
                total = calculate_total(cart)
                print(f"Total Amount: ${total}")
                save_invoice(cart)
                break
            else:
                print("Cart is empty! Add items before checkout.")
        elif choice == '6':
            print("Exiting... Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the store management system
if __name__ == "__main__":
    store_management_system()
