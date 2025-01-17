class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Inheriting from Animal
    def speak(self):  # Overriding the parent method
        print(f"{self.name} says Woof!")

# Create objects
animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound.

dog = Dog("Buddy")
dog.speak()  # Output: Buddy says Woof!
