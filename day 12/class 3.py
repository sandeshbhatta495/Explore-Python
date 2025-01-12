class FileHandler:
    # Constructor to initialize a file
    def __init__(self, filename):
        self.file = open(filename, "w")
        print("File opened for writing.")

    # Destructor to close the file
    def __del__(self):
        self.file.close()
        print("File closed.")

# Creating and using the object
file_obj = FileHandler("example.txt")
file_obj.file.write("Hello, Python!")
del file_obj  # Explicitly calling the destructor
