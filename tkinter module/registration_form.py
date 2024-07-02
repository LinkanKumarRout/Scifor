import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    address = address_entry.get("1.0", "end-1c")  # Retrieve text from Text widget
    email = email_entry.get()
    contact = contact_entry.get()
    country = country_entry.get()
    state = state_entry.get()
    diseases = [disease_vars[i].get() for i in range(len(disease_vars))]

    messagebox.showinfo("Registration Successful", "Thank you for registering!")

root = tk.Tk()
root.title("COVID Vaccine Registration Form")

# Labels and Entries
labels = ["Name:", "Age:", "Gender:", "Address:", "Email ID:", "Contact No:", "Country:", "State:"]
for i, label_text in enumerate(labels):
    tk.Label(root, text=label_text).grid(row=i, column=0, padx=10, pady=5)
    if label_text == "Gender:":
        gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=i, column=1)
        tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=i, column=2)
    elif label_text == "Address:":
        address_entry = tk.Text(root, height=4, width=20)
        address_entry.grid(row=i, column=1, columnspan=2)
    else:
        entry = tk.Entry(root)
        entry.grid(row=i, column=1, columnspan=2)
        if label_text == "Name:":
            name_entry = entry
        elif label_text == "Age:":
            age_entry = entry
        elif label_text == "Email ID:":
            email_entry = entry
        elif label_text == "Contact No:":
            contact_entry = entry
        elif label_text == "Country:":
            country_entry = entry
        elif label_text == "State:":
            state_entry = entry

# Checkboxes for diseases
disease_vars = [tk.BooleanVar() for _ in range(4)]
disease_labels = ["Cold", "Cough", "Fever", "Headache"]
for i, disease_label in enumerate(disease_labels):
    tk.Checkbutton(root, text=disease_label, variable=disease_vars[i]).grid(row=len(labels), column=i, padx=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=len(labels)+1, columnspan=3, pady=10)

root.mainloop()
