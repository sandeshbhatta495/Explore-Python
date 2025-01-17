from PIL import Image, ImageTk  
from tkinter import *  
from courses import Courses 
# Importing PIL library for handling images # Importing all components from tkinter for GUI development  # Import the Courses class from courses.py
class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")  # Setting the title of the window
        self.root.geometry("1375x700+0+0")  # Setting the window size and position
        self.root.config(bg="white")  # Setting the background color of the window

        # Load the logo image
        self.logo_dash = ImageTk.PhotoImage(
            file=r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2025-01-12 235624.png"
        )

                # Title
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, font=("times new roman", 35, "bold","underline"), bg="Blue", fg="White")
        title.place(x=0, y=0, relwidth=1, height=70)


        #right corner image
        self.bg =  self.Image.open( file = r"C:\Users\DELL\Desktop\logo.png")
        self.bg = self.bg.resize((500, 500), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.bg)
        bg = Label(self.root, image=self.bg).place(x=1000, y=100, width=500, height=500)
        


        

         # Frame for buttons (with border)
        menu_frame = Frame(self.root, bg="White", bd=2, relief=SOLID)
        menu_frame.place(x=50, y=70, width=1200, height=75)
        # Buttons
        
        btn_course = Button(self.root, text="Courses", command=self.courses, font=("times new roman", 20, "bold"), bg="White", fg="black", cursor="hand2")
        btn_course.place(x=55, y=80, width=200, height=50)

        btn_student = Button(self.root, text="Students", command=self.Student, font=("times new roman", 20, "bold"), bg="white", fg="black", cursor="hand2")
        btn_student.place(x=300, y=80, width=200, height=50)

        btn_result = Button(self.root, text="Results", command=self.results, font=("times new roman", 20, "bold"), bg="white", fg="black", cursor="hand2")
        btn_result.place(x=545, y=80, width=200, height=50)

        btn_view_result = Button(self.root, text="View Results", command=self.btn_view_result, font=("Times new roman", 20, "bold"), bg="white", fg="black", cursor="hand2")
        btn_view_result.place(x=790, y=80, width=200, height=50)

        btn_logout = Button(self.root, text="Log Out", command=self.logout, font=("times new roman", 20, "bold"), bg="white", fg="black", cursor="hand2")
        btn_logout.place(x=1035, y=80, width=200, height=50)

        btn_exit = Button(self.root, text="Exit", command=self.exit_app, font=("times new roman", 20, "bold"), bg="White", fg="black", cursor="hand2")
        btn_exit.place(x=1280, y=80, width=200, height=50)

        # Total Courses
        self.label_total_courses = Label(self.root, text="Total Courses [0]", font=("times new roman", 20, "bold"), bg="Orange", fg="white", cursor="hand2")
        self.label_total_courses.place(x=350, y=490, width=250, height=40)

        # Total Results
        self.label_total_results = Label(self.root, text="Total Results [0]", font=("times new roman", 20, "bold"), bg="Blue", fg="white", cursor="hand2")
        self.label_total_results.place(x=700, y=490, width=250, height=40)

        # Total Students
        self.label_total_students = Label(self.root, text="Total Students [0]", font=("times new roman", 20, "bold"), bg="Green", fg="white", cursor="hand2")
        self.label_total_students.place(x=1050, y=490, width=250, height=40)

        # Footer
        footer = Label(self.root, text="Developed by: Sandesh Bhatta\nStudent Result Management System\nAny Technical Issue: 974168****", font=("times new roman", 10), bg="Red", fg="white")
        footer.place(x=0, y=580, relwidth=1, height=75)


           

    # Placeholder methods for button commands
    def courses(self):
        self.__new__window= Toplevel(self.root)
        self.new_obj = Courses(self.__new__window)
        print("Courses button clicked.")

    def Student(self):
        print("Students button clicked.")

    def results(self):
        print("Results button clicked.")

    def btn_view_result(self):
        print("View Results button clicked.")

    def logout(self):
        print("Log Out button clicked.")

    def exit_app(self):
        self.root.destroy()  # Close the application


# Run the application
if __name__ == "__main__":
    root = Tk()  # Create the main tkinter window
    obj = RMS(root)  # Create an instance of the RMS class and pass the root window to it
    root.mainloop()  # Start the tkinter event loop
