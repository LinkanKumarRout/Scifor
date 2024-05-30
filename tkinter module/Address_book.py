import tkinter as tk
from tkinter import messagebox
from tkinter import font

root = tk.Tk()
root.title("Address Book")

contacts = {}
def get_selected_contact():
  name = name_entry.get()

  if name in contacts:
    messagebox.showinfo("Contact", f"Name: {name}\nPhone: {contacts[name]}")
  else:
    messagebox.showwarning("Error", "Contact not found")

def add_contact():
  name = name_entry.get()
  number = number_entry.get()

  contacts[name] = number
  messagebox.showinfo("Success", "Contact added successfully !!")


def view_contact():
  all_contacts = ""
  for name, number in contacts.items():
    all_contacts += f"Name: {name}\nPhone: {number}\n\n"

  if all_contacts:
    messagebox.showinfo("All Contacts", all_contacts)
  else:
    messagebox.showwarning("Error", "No contact found")

def edit_contact():
  name = name_entry.get()

  if name in contacts:
    new_number = number_entry.get()
    contacts[name] = new_number
    messagebox.showinfo("Success", "Contact Updated")

def exit():
  root.quit()

def reset():
  name_entry.delete(0, tk.END)
  number_entry.delete(0, tk.END)

frame = tk.Frame(root, bg="lightblue")
frame.pack()

title1 = tk.Label(frame, text="Enter Details")
title1.grid(row=0, column=0, columnspan=2)

name_label = tk.Label(frame, text="Name: ")
name_label.grid(row=1, column=0, sticky="W")
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=1, column=1, padx=10)

number_label = tk.Label(frame, text="Mob: ")
number_label.grid(row=2, column=0, sticky="W")
number_entry = tk.Entry(frame, font=("Arial", 12))
number_entry.grid(row=2, column=1, padx=10)


get_selected_btn = tk.Button(frame, text="Get Selected Contact", command=get_selected_contact)
get_selected_btn.grid(row=3, column=0, columnspan=2, pady=10)

add_contact_btn = tk.Button(frame, text="Add Contact", command=add_contact)
add_contact_btn.grid(row=4, column=0, columnspan=2, pady=10)

view_contact_btn = tk.Button(frame, text="View Contact", command=view_contact)
view_contact_btn.grid(row=5, column=0, columnspan=2, pady=10)

edit_contact_btn = tk.Button(frame, text="Edit Contact", command=edit_contact)
edit_contact_btn.grid(row=6, column=0, columnspan=2, pady=10)

reset_btn = tk.Button(frame, text="Reset", command=reset)
reset_btn.grid(row=7, column=0, columnspan=2, pady=10)

exit_btn = tk.Button(frame, text="Exit", command=exit)
exit_btn.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()