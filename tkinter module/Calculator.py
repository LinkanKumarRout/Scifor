import tkinter as tk

root = tk.Tk()
root.title("Advanced Calculator")

clear_entry = False
def button_click(value):
    current = screen.get()
    global clear_entry
    if clear_entry:
        screen.delete(0, tk.END)
        clear_entry = False

    if value == "C":
        screen.delete(0, tk.END)
    elif value == "=":
        result = evaluate_expression(current)
        screen.delete(0, tk.END)
        screen.insert(0, str(result))
        clear_entry = True
    else:
        screen.insert(tk.END, value)

def evaluate_expression(expression):
    if expression:
        return eval(expression)
    else:
        return "Error"

frame = tk.Frame(root, bg="lightblue")
frame.pack()

title1 = tk.Label(frame, text="Calculator", fg="black", bg="lightblue", font=("Arial", 15))
title1.grid(row=0, column=0, columnspan=4)

screen = tk.Entry(frame, font=("Arial", 30), borderwidth=2)
screen.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("C", 6, 1)
]

for (text, row, column) in buttons:
    button = tk.Button(frame, text=text, font=("Arial", 20),width=4, fg="black", bg="white", command= lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=10, pady=10)

root.mainloop()