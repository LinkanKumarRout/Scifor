import tkinter as tk
from tkinter import messagebox

# Function to validate and process registration
def validate():
    name_val = name_entry.get()
    age_val = age_entry.get()
    gender_val = gender.get()
    address_val = address_entry.get("1.0", "end-1c")  # Get text from the Text widget
    email_val = email_entry.get()
    contact_val = contact_entry.get()
    country_val = country_entry.get()
    state_val = state_entry.get()
    diseases_val = [disease_vars[i].get() for i in range(len(disease_vars))]

    if all([name_val, age_val, gender_val, address_val, email_val, contact_val, country_val, state_val]) and any(diseases_val):
        message = f"Registration Successful for {name_val}"
        messagebox.showinfo("Success !!", message)
        clear()
    else:
        messagebox.showerror("Error", "Please fill all the details")

# Function to clear all entries
def clear():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)
    state_entry.delete(0, tk.END)
    for disease_var in disease_vars:
        disease_var.set(False)

# Create the main window
root = tk.Tk()
root.title("COVID Vaccine Registration Form")

# Create a frame to hold widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Title
title = tk.Label(frame, text="Enter your information below:", font=("Arial", 12))
title.grid(row=0, column=0, columnspan=2)

# Name
name_label = tk.Label(frame, text="Name: ", font=("Arial", 12))
name_label.grid(row=1, column=0, sticky="W")
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=1, column=1)

# Age
age_label = tk.Label(frame, text="Age: ", font=("Arial", 12))
age_label.grid(row=2, column=0, sticky="W")
age_entry = tk.Entry(frame, font=("Arial", 12))
age_entry.grid(row=2, column=1)

# Gender
gender_label = tk.Label(frame, text="Gender: ", font=("Arial", 12))
gender_label.grid(row=3, column=0, sticky="W")
gender = tk.StringVar()  # Create a StringVar to hold the selected gender
gender.set("Male")  # Set default value
male_radio = tk.Radiobutton(frame, text="Male", value="Male", variable=gender)
male_radio.grid(row=3, column=1, sticky="W")
female_radio = tk.Radiobutton(frame, text="Female", value="Female", variable=gender)
female_radio.grid(row=3, column=2, sticky="W")

# Address
address_label = tk.Label(frame, text="Address: ", font=("Arial", 12))
address_label.grid(row=4, column=0, sticky="W")
address_entry = tk.Text(frame, font=("Arial", 12), height=4, width=30)
address_entry.grid(row=4, column=1)

# Email
email_label = tk.Label(frame, text="Email: ", font=("Arial", 12))
email_label.grid(row=5, column=0, sticky="W")
email_entry = tk.Entry(frame, font=("Arial", 12))
email_entry.grid(row=5, column=1)

# Contact No.
contact_label = tk.Label(frame, text="Contact No.: ", font=("Arial", 12))
contact_label.grid(row=6, column=0, sticky="W")
contact_entry = tk.Entry(frame, font=("Arial", 12))
contact_entry.grid(row=6, column=1)

# Country
country_label = tk.Label(frame, text="Country: ", font=("Arial", 12))
country_label.grid(row=7, column=0, sticky="W")
country_entry = tk.Entry(frame, font=("Arial", 12))
country_entry.grid(row=7, column=1)

# State
state_label = tk.Label(frame, text="State: ", font=("Arial", 12))
state_label.grid(row=8, column=0, sticky="W")
state_entry = tk.Entry(frame, font=("Arial", 12))
state_entry.grid(row=8, column=1)

# Diseases
disease_label = tk.Label(frame, text="Select disease(s): ", font=("Arial", 12))
disease_label.grid(row=9, column=0, sticky="W")

disease_vars = []  # List to hold BooleanVars for diseases
diseases = ["Cold", "Cough", "Fever", "Headache"]
for i, disease_name in enumerate(diseases):
    disease_var = tk.BooleanVar()  # Create a BooleanVar for each disease
    disease_vars.append(disease_var)
    disease_checkbox = tk.Checkbutton(frame, text=disease_name, variable=disease_var)
    disease_checkbox.grid(row=9, column=i+1, sticky="W")

# Submit button
submit_btn = tk.Button(frame, text="Submit", font=("Arial", 12), fg="black", bg="green", command=validate)
submit_btn.grid(row=10, column=0)

# Clear button
clear_btn = tk.Button(frame, text="Clear", font=("Arial", 12), fg="black", bg="red", command=clear)
clear_btn.grid(row=10, column=1)

# Start the GUI event loop
root.mainloop()