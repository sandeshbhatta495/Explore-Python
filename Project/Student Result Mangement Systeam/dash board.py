from PIL import Image, ImageTk
from tkinter import*

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Title
        title = Label(
            self.root,
            text="Student Result Management System"padx=10,compound=LEFT,image=self.logo_dash,font=("times new roman", 40, "bold"),bg="white",
            fg="black").place(x=0, y=0, relwidth=1, height=50)

        # Icons
        self.logo_dash = ImageTk.PhotoImage(
            file=r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2025-01-12 235624.png"
        )
        
# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
