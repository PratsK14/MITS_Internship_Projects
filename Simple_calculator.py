import tkinter as tk
from tkinter import messagebox
import re

history = []  # To store past calculations

def evaluate_expression():
    expr = entry.get().replace(" ", "")

    if not re.fullmatch(r"[0-9+\-*/().]+", expr):
        messagebox.showerror("Invalid Input", "Only numbers and + - * / ( ) are allowed.")
        return

    try:
        result = eval(expr)
        result_label.config(text=f"Result: {result}")
        history.append(f"{expr} = {result}")
    except ZeroDivisionError:
        result_label.config(text="Error: Division by zero.")
    except Exception:
        result_label.config(text="Error: Invalid expression.")

def show_history():
    if not history:
        messagebox.showinfo("History", "No history available.")
    else:
        messagebox.showinfo("History", "\n".join(history[-10:]))

def add_to_entry(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

def handle_keypress(event):
    if event.keysym == "Return":
        evaluate_expression()
    elif event.keysym == "Escape":
        clear_entry()

# --- GUI Setup ---
root = tk.Tk()
root.title("Smart Tkinter Calculator")
root.geometry("360x420")

entry = tk.Entry(root, font=("Arial", 20), width=22, borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.bind("<Key>", handle_keypress)

result_label = tk.Label(root, text="Result:", font=("Arial", 16))
result_label.grid(row=1, column=0, columnspan=4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '(', '+'),
    (')', 'C', '=', 'H')  # H for history
]

for r, row in enumerate(buttons, 2):
    for c, char in enumerate(row):
        if char == '=':
            action = evaluate_expression
        elif char == 'C':
            action = clear_entry
        elif char == 'H':
            action = show_history
        else:
            action = lambda val=char: add_to_entry(val)

        tk.Button(root, text=char, font=("Arial", 16), width=5, command=action).grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
