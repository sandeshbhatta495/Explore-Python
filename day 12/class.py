class Person:
    # Constructor (__init__)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Constructor called for {self.name}")

# Create objects
person1 = Person("Alice", 25)  # Constructor automatically called
person2 = Person("Bob", 30)
