class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def get_balance(self):  # Getter
        return self.__balance

    def deposit(self, amount):  # Setter
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

# Create object
account = BankAccount("John", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)  # Output: Deposited 500. New balance: 1500
