from tkinter import Tk, Label
from PIL import Image, ImageTk

# Create the main window
root = Tk()
root.geometry("800x600")  # Set the window size (adjust as needed)

# Load and process the image
image_path = r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2025-01-12 235624.png"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)
bg_image_tk = ImageTk.PhotoImage(bg_image)

# Create a label to hold the image
bg_label = Label(root, image=bg_image_tk)
bg_label.image = bg_image_tk  # Keep a reference to prevent garbage collection

# Place the image label in the bottom-right corner
bg_label.place(relx=1.0, rely=1.0, anchor="se")  # Adjust `anchor` for alignment
# `relx=1.0` and `rely=1.0` position the label at the bottom-right corner

# Start the GUI loop
root.mainloop()
