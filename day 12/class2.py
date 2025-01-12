class MyClass:
    def __init__(self):
        print("Constructor called.")
    
    def __del__(self):
        print("Destructor called. Object deleted.")

# Creating and deleting an object
obj = MyClass()
del obj  # Explicitly delete the object
