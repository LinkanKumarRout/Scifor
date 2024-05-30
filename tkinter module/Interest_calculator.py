from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Interest Calculator")

title= Label(root, text="Interest Claculator", font=("Arial",12))
title.grid(row=0, column=0, columnspan=2)

interest_type = StringVar()
simple_radio = Radiobutton(root, text="Simple Interest", variable=interest_type, value="Simple Interest").grid(row=1, column=0, sticky="W")
compound_radio = Radiobutton(root, text="Compound Interest", variable=interest_type, value="Compound Interest").grid(row=1, column=1, sticky="W")
interest_type.set("Simple Interest")

# principal
principal_label = Label(root, text="Principal: ").grid(row=2, column=0, sticky="W")
principal_entry = Entry(root)
principal_entry.grid(row=2, column=1)

# rate of interest
rate_label = Label(root, text="Rate: ").grid(row=3, column=0, sticky="W")
rate_entry = Entry(root)
rate_entry.grid(row=3, column=1)

# time
time_label = Label(root, text="Time: ").grid(row=4, column=0, sticky="W")
time_entry = Entry(root)
time_entry.grid(row=4, column=1)

def cal_interest():
  principal_val = principal_entry.get()
  rate_val = rate_entry.get()
  time_val = time_entry.get()
  if not (principal_val and rate_val and time_val):
    messagebox.showerror("Error", "Please enter all details")

  principal = float(principal_val)
  rate = float(rate_val)
  time = float(time_val)

  if interest_type.get() == "Simple Interest":
    interest = (principal * time * rate)/100
  else:
    interest = principal * ((1 + rate/100)**time -1)
  message = f"Your Interest is {round(interest, 2)}"
  messagebox.showinfo("Interest", message)

calc_btn = Button(root, text="Calculate", fg="black", bg="green", command=cal_interest).grid(row=5, column=0, columnspan=2)

root.mainloop()