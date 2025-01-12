#in this code i learn about class and object and how to create class and object in python
class introduction:
    #constructor of class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #method to define a function inside the class
    def input(self):
        self.name = input("Enter Your Name: ")
        self.age = int(input("Enter Your Age: "))
    def output(self):
        print(f"My Name is {self.name} and I am {self.age} years old")

        

#creating object of class
nameobj=introduction()
#calling the function
nameobj.input()
nameobj.output()

        