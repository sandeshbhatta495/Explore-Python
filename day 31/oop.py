# In this code, I learn about class and objects and how to create them in Python
class Introduction:
    # Constructor of the class
    def __init__(self, name=None, age=None):  # Optional parameters
        self.name = name
        self.age = age

    # Method to take input for name and age
    def input(self):
        self.name = input("Enter Your Name: ")
        self.age = int(input("Enter Your Age: "))

    # Method to display output
    def output(self):
        print(f"My Name is {self.name} and I am {self.age} years old.")


# Creating object of the class
nameobj = Introduction()  # Create an object with no arguments

# Calling the methods
nameobj.input()  # Prompt for user input
nameobj.output()  # Display the entered information
