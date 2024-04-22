import tkinter as tk
from tkinter import messagebox

# check registration
def validate():
  name_val = name_entry.get()
  age_val = age_entry.get()
  gender_val = gender.get()
  address_val = address_entry.get()
  email_val = email_entry.get()
  contact_val = contact_entry.get()
  country_val = country_entry.get()
  state_val = state_entry.get()
  disease_val = disease.get()

  if name_val and age_val and gender_val and address_val and email_val and contact_val and country_val and state_val and disease_val:
    message = f"Registration Successful for {name_val}"
    messagebox.showinfo("Success !!", message)
    clear()
  else:
    messagebox.showerror("Error", "Please fill all the details")
  
  

def clear():
  name_entry.delete(0, tk.END)

root = tk.Tk()
root.title("COVID Vaccine Registration Form")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

title = tk.Label(frame, text="Enter your information below:", font=("Arial", 12))
title.grid(row=0, column=0, columnspan=2)
# Name
name_label = tk.Label(frame, text="Name: ", font=("Arial", 12))
name_label.grid(row = 1, column=0, sticky="W")
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=1, column=1)
# Age
age_label = tk.Label(frame, text="Age: ", font=("Arial", 12))
age_label.grid(row = 2, column=0, sticky="W")
age_entry = tk.Entry(frame, font=("Arial", 12))
age_entry.grid(row=2, column=1)
# Gender
gender_label = tk.Label(frame, text="Gender: ", font=("Arial",12))
gender_label.grid(row=3, column=0, sticky="W")

gender = tk.Radiobutton(frame, text="Male", value="Male").grid(row=3, column=1, sticky="W") or tk.Radiobutton(frame, text="Female", value="Female").grid(row=3, column=2, sticky="W")

# Address
address_label = tk.Label(frame, text="Address: ", font=("Arial", 12))
address_label.grid(row = 4, column=0, sticky="W")
address_entry = tk.Text(frame, font=("Arial", 12), height=4, width=30)
address_entry.grid(row=4, column=1)
# Email
email_label = tk.Label(frame, text="Email: ", font=("Arial", 12))
email_label.grid(row = 5, column=0, sticky="W")
email_entry = tk.Entry(frame, font=("Arial", 12))
email_entry.grid(row=5, column=1)
# Contact No.
contact_label = tk.Label(frame, text="Contact No.: ", font=("Arial", 12))
contact_label.grid(row = 6, column=0, sticky="W")
contact_entry = tk.Entry(frame, font=("Arial", 12))
contact_entry.grid(row=6, column=1)
# Country
country_label = tk.Label(frame, text="Country: ", font=("Arial", 12))
country_label.grid(row = 7, column=0, sticky="W")
country_entry = tk.Entry(frame, font=("Arial", 12))
country_entry.grid(row=7, column=1)
# State
state_label = tk.Label(frame, text="State: ", font=("Arial", 12))
state_label.grid(row = 8, column=0, sticky="W")
state_entry = tk.Entry(frame, font=("Arial", 12))
state_entry.grid(row=8, column=1)
# Diseases
disease_label = tk.Label(frame, text="Select a disease: ",font=("Arial", 12))
disease_label.grid(row=9, column=0, sticky="W")
disease = tk.Checkbutton(frame, text="Cold", variable=tk.IntVar()).grid(row=9, column=1, sticky="W") or tk.Checkbutton(frame, text="Cough", variable=tk.IntVar()).grid(row=9, column=2, sticky="W") or tk.Checkbutton(frame, text="Fever", variable=tk.IntVar()).grid(row=9, column=3, sticky="W") or tk.Checkbutton(frame, text="Headache", variable=tk.IntVar()).grid(row=9, column=4, sticky="W")


# submit
submit_btn = tk.Button(frame, text="Submit", font=("Arial", 12), fg="black", bg="green", command = validate)
submit_btn.grid(row=10, column=0)
# Clear
clear_btn = tk.Button(frame, text="Clear", font=("Arial", 12), fg="black", bg="red", command=clear)
clear_btn.grid(row=10, column=1)

root.mainloop()