import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, roll, name, grade):
        self.roll = roll
        self.name = name
        self.grade = grade

    def display_details(self):
        return f"Roll: {self.roll}\nName: {self.name}\nGrade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, roll, name, grade):
        if roll.strip() == '' or name.strip() == '' or grade.strip() == '':
            return "Error! Please fill in all fields."

        if not roll.isdigit():
            return "Error! Roll number must be a number."

        roll = int(roll)
        if roll in self.students:
            return "Error! Student with the same roll number already exists."

        self.students[roll] = Student(roll, name, grade)
        return "Student added successfully."

    def display_students(self):
        if not self.students:
            return "No students found."

        all_details = ""
        for roll, student in self.students.items():
            all_details += student.display_details() + "\n\n"
        return all_details

    def search_student(self, roll):
        if not roll.isdigit():
            return "Error! Roll number must be a number."

        roll = int(roll)
        student = self.students.get(roll)
        if student:
            return student.display_details()
        else:
            return "Error! Student not found."

    def update_student(self, roll, name, grade):
        if not roll.isdigit():
            return "Error! Roll number must be a number."

        roll = int(roll)
        if roll not in self.students:
            return "Error! Student not found."

        self.students[roll].name = name
        self.students[roll].grade = grade
        return "Student details updated successfully."

    def delete_student(self, roll):
        if not roll.isdigit():
            return "Error! Roll number must be a number."

        roll = int(roll)
        if roll not in self.students:
            return "Error! Student not found."

        del self.students[roll]
        return "Student deleted successfully."

obj = StudentManagementSystem()

def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    grade = grade_entry.get()
    messagebox.showinfo("Result", obj.add_student(roll, name, grade))

def view_students():
    messagebox.showinfo("All Students", obj.display_students())

def search_student():
    roll = roll_entry.get()
    messagebox.showinfo("Search Result", obj.search_student(roll))

def update_student():
    roll = roll_entry.get()
    name = name_entry.get()
    grade = grade_entry.get()
    messagebox.showinfo("Result", obj.update_student(roll, name, grade))

def delete_student():
    roll = roll_entry.get()
    messagebox.showinfo("Result", obj.delete_student(roll))

root = tk.Tk()
root.title("Student Management System")
root.config(bg="lightblue")

frame = tk.Frame(root)
frame.pack()

roll_label = tk.Label(frame, text="Roll:", font=("Arial", 12))
roll_label.grid(row=0, column=0,padx=10, pady=10, sticky="W")
roll_entry = tk.Entry(frame)
roll_entry.grid(row=0, column=1,padx=10, pady=10)

name_label = tk.Label(frame, text="Name:", font=("Arial", 12))
name_label.grid(row=1, column=0,padx=10, pady=10, sticky="W")
name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=1,padx=10, pady=10)

grade_label = tk.Label(frame, text="Grade:", font=("Arial", 12))
grade_label.grid(row=2, column=0,padx=10, pady=10, sticky="W")
grade_entry = tk.Entry(frame)
grade_entry.grid(row=2, column=1,padx=10, pady=10)

add_button = tk.Button(frame, text="Add Student", font=("Arial", 12), command=add_student)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

view_button = tk.Button(frame, text="All Students", font=("Arial", 12), command=view_students)
view_button.grid(row=4, column=0, columnspan=2, pady=10)

search_button = tk.Button(frame, text="Search Student", font=("Arial", 12), command=search_student)
search_button.grid(row=5, column=0, columnspan=2, pady=10)

update_button = tk.Button(frame, text="Update Student", font=("Arial", 12), command=update_student)
update_button.grid(row=6, column=0, columnspan=2, pady=10)

delete_button = tk.Button(frame, text="Delete Student", font=("Arial", 12), command=delete_student)
delete_button.grid(row=7, column=0, columnspan=2, pady=10)

exit_button = tk.Button(frame, text="Exit", font=("Arial", 12), command=root.destroy)
exit_button.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()