from tkinter import *
from PIL import Image, ImageTk
from courses import Courses  # Ensure this is properly defined in the same project

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1360x700+0+0")
        self.root.config(bg="white")

        # Logo in title
        self.logo_image = Image.open(r"C:\Users\DELL\Desktop\logo.png")
        self.logo_image = self.logo_image.resize((50, 50), Image.LANCZOS)  # Updated resizing method
        self.logo_dash = ImageTk.PhotoImage(self.logo_image)

        # Title bar
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("times new roman", 40, "bold"), bg="blue", fg="white")
        title.place(x=0, y=0, relwidth=1, height=60)

        # Menu Frame
        menu_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        menu_frame.place(x=10, y=70, width=1330, height=80)

        # Menu Buttons
        Button(menu_frame, text="Courses", font=("times new roman", 20, "bold"),
               bg="white", fg="black", cursor="hand2", command=self.courses).place(x=20, y=20, width=150, height=40)

        Button(menu_frame, text="Students", font=("times new roman", 20, "bold"),
               bg="white", fg="black", cursor="hand2", command=self.student).place(x=200, y=20, width=150, height=40)

        Button(menu_frame, text="Results", font=("times new roman", 20, "bold"),
               bg="white", fg="black", cursor="hand2", command=self.results).place(x=380, y=20, width=150, height=40)

        Button(menu_frame, text="View Results", font=("times new roman", 20, "bold"),
               bg="white", fg="black", cursor="hand2", command=self.view_results).place(x=560, y=20, width=200, height=40)

        Button(menu_frame, text="Logout", font=("times new roman", 20, "bold"),
               bg="white", fg="black", cursor="hand2", command=self.logout).place(x=800, y=20, width=150, height=40)

        Button(menu_frame, text="Exit", font=("times new roman", 20, "bold"),
               bg="white", fg="black", cursor="hand2", command=self.exit_app).place(x=980, y=20, width=150, height=40)

        # Info Labels
        Label(self.root, text="Total Courses [0]", font=("times new roman", 20, "bold"),
              bg="orange", fg="white", cursor="hand2").place(x=350, y=490, width=250, height=40)

        Label(self.root, text="Total Results [0]", font=("times new roman", 20, "bold"),
              bg="blue", fg="white", cursor="hand2").place(x=700, y=490, width=250, height=40)

        Label(self.root, text="Total Students [0]", font=("times new roman", 20, "bold"),
              bg="green", fg="white", cursor="hand2").place(x=1050, y=490, width=250, height=40)

        # Footer
        footer = Label(self.root, text="Developed by: Sandesh Bhatta", font=("times new roman", 15),
                       bg="blue", fg="red")
        footer.pack(side=BOTTOM, fill=X)

    # Function Definitions
    def courses(self):
        print("Courses button clicked")
        # Open a new window for Courses
        new_window = Toplevel(self.root)
        Courses(new_window)

    def student(self):
        print("Student button clicked")  # Placeholder for student functionality

    def results(self):
        print("Results button clicked")  # Placeholder for results functionality

    def view_results(self):
        print("View Results button clicked")  # Placeholder for view results functionality

    def logout(self):
        print("Logout button clicked")  # Placeholder for logout functionality

    def exit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
