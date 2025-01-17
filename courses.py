from tkinter import *

class Courses:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.build_course_page()

    def build_course_page(self):
        # Title
        course_title = Label(self.parent_frame, text="Courses Management",
                             font=("times new roman", 30, "bold"), bg="white", fg="blue")
        course_title.pack(pady=10)

        # Frame for Course Details (Left Side)
        course_frame = Frame(self.parent_frame, bg="white", bd=2, relief=RIDGE)
        course_frame.place(x=20, y=80, width=700, height=380)

        # Course Name
        lbl_course_name = Label(course_frame, text="Course Name:",
                                font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_course_name.grid(row=0, column=0, padx=20, pady=10, sticky=W)

        self.entry_course_name = Entry(course_frame, font=("times new roman", 15), bg="lightyellow")
        self.entry_course_name.grid(row=0, column=1, padx=20, pady=10, sticky=W)

        # Course Duration
        lbl_course_duration = Label(course_frame, text="Duration:",
                                     font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_course_duration.grid(row=1, column=0, padx=20, pady=10, sticky=W)

        self.entry_course_duration = Entry(course_frame, font=("times new roman", 15), bg="lightyellow")
        self.entry_course_duration.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        # Course Fee
        lbl_course_fee = Label(course_frame, text="Fee:",
                                font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_course_fee.grid(row=2, column=0, padx=20, pady=10, sticky=W)

        self.entry_course_fee = Entry(course_frame, font=("times new roman", 15), bg="lightyellow")
        self.entry_course_fee.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        # Course Description
        lbl_course_description = Label(course_frame, text="Description:",
                                        font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_course_description.grid(row=3, column=0, padx=20, pady=10, sticky=NW)

        self.text_course_description = Text(course_frame, font=("times new roman", 15), bg="lightyellow", height=5, width=50)
        self.text_course_description.grid(row=3, column=1, padx=20, pady=10, sticky=W)

        # Save Button
        btn_save = Button(course_frame, text="Save", font=("times new roman", 15, "bold"),
                          bg="green", fg="white", command=self.save_course)
        btn_save.grid(row=4, column=0, padx=20, pady=20, sticky=W)

        # Clear Button
        btn_clear = Button(course_frame, text="Clear", font=("times new roman", 15, "bold"),
                           bg="red", fg="white", command=self.clear_inputs)
        btn_clear.grid(row=4, column=1, padx=20, pady=20, sticky=W)

        # Frame for Search and Course List (Right Side)
        right_frame = Frame(self.parent_frame, bg="white", bd=2, relief=RIDGE)
        right_frame.place(x=740, y=80, width=540, height=380)

        # Search Bar
        lbl_search = Label(right_frame, text="Search Course:", font=("times new roman", 15, "bold"),
                           bg="white", fg="black")
        lbl_search.pack(pady=10)

        self.entry_search = Entry(right_frame, font=("times new roman", 15), bg="lightyellow", width=30)
        self.entry_search.pack(pady=10)

        btn_search = Button(right_frame, text="Search", font=("times new roman", 15, "bold"),
                            bg="blue", fg="white", command=self.search_course)
        btn_search.pack(pady=10, fill=X)

        # Update and Delete Buttons
        btn_update = Button(right_frame, text="Update", font=("times new roman", 15, "bold"),
                            bg="orange", fg="white", command=self.update_course)
        btn_update.pack(pady=10, fill=X)

        btn_delete = Button(right_frame, text="Delete", font=("times new roman", 15, "bold"),
                            bg="red", fg="white", command=self.delete_course)
        btn_delete.pack(pady=10, fill=X)

        # Placeholder for List of Courses
        course_list_title = Label(right_frame, text="List of Courses",
                                  font=("times new roman", 20, "bold"), bg="white", fg="purple")
        course_list_title.pack(pady=5)

        # Add a scrollbar and listbox for course display
        self.course_listbox = Listbox(right_frame, font=("times new roman", 15),
                                      bg="lightyellow", fg="black", selectmode=SINGLE)
        self.course_listbox.pack(fill=BOTH, expand=True, padx=10, pady=5)

    def save_course(self):
        # Save the course details (example: adding to the listbox)
        name = self.entry_course_name.get()
        duration = self.entry_course_duration.get()
        fee = self.entry_course_fee.get()
        description = self.text_course_description.get("1.0", END).strip()

        if name and duration and fee:  # Ensure all fields are filled
            course_details = f"{name} | {duration} | {fee} | {description}"
            self.course_listbox.insert(END, course_details)
            self.clear_inputs()  # Clear input fields after saving
        else:
            print("Please fill all fields!")  # You can use a messagebox instead

    def clear_inputs(self):
        self.entry_course_name.delete(0, END)
        self.entry_course_duration.delete(0, END)
        self.entry_course_fee.delete(0, END)
        self.text_course_description.delete("1.0", END)

    def delete_course(self):
        # Delete the selected course
        selected = self.course_listbox.curselection()
        if selected:
            self.course_listbox.delete(selected)

    def update_course(self):
        # Update the selected course
        selected = self.course_listbox.curselection()
        if selected:
            course_details = self.course_listbox.get(selected)
            parts = course_details.split(" | ")
            self.entry_course_name.delete(0, END)
            self.entry_course_name.insert(0, parts[0])
            self.entry_course_duration.delete(0, END)
            self.entry_course_duration.insert(0, parts[1])
            self.entry_course_fee.delete(0, END)
            self.entry_course_fee.insert(0, parts[2])
            self.text_course_description.delete("1.0", END)
            self.text_course_description.insert("1.0", parts[3])
            self.course_listbox.delete(selected)

    def search_course(self):
        # Search for a course by name
        search_term = self.entry_search.get().lower()
        self.course_listbox.delete(0, END)
        for course in self.get_all_courses():
            if search_term in course.lower():
                self.course_listbox.insert(END, course)

    def get_all_courses(self):
        # Get all courses currently in the listbox
        return [self.course_listbox.get(i) for i in range(self.course_listbox.size())]
