# Define a class
class Car:
    # Constructor method (__init__) to initialize attributes
    def __init__(self, brand, color):
        self.brand = brand  # Attribute 1
        self.color = color  # Attribute 2
    
    # A method (function) inside the class
    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")
    
    def stop(self):
        print(f"The {self.brand} has stopped.")

# Create objects (instances of the class)
car1 = Car("Toyota", "red")  # Object 1
car2 = Car("Honda", "blue")  # Object 2

# Access attributes and call methods using objects
print(car1.brand)  # Output: Toyota
print(car2.color)  # Output: blue

car1.drive()  # Output: The red Toyota is driving.
car2.stop()   # Output: The Honda has stopped.
