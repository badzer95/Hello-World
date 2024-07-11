import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

def button_sin():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

def button_cos():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

def button_tan():
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

def button_log():
    try:
        result = math.log10(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

def button_ln():
    try:
        result = math.log(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

button_dict = {
    '0': (5, 0), '1': (4, 0), '2': (4, 1), '3': (4, 2),
    '4': (3, 0), '5': (3, 1), '6': (3, 2), '7': (2, 0),
    '8': (2, 1), '9': (2, 2), '+': (5, 3), '-': (4, 3),
    '*': (3, 3), '/': (2, 3), '.': (5, 1), '(': (1, 0),
    ')': (1, 1), 'sin': (1, 2), 'cos': (1, 3), 'tan': (1, 4),
    'log': (1, 5), 'ln': (1, 6), '^': (2, 4), '√': (2, 5),
}

for symbol, grid_pos in button_dict.items():
    if symbol in '0123456789+-*/().':
        button = tk.Button(root, text=symbol, padx=20, pady=20, command=lambda symbol=symbol: button_click(symbol))
    elif symbol == 'sin':
        button = tk.Button(root, text=symbol, padx=20, pady=20, command=button_sin)
    elif symbol == 'cos':
        button = tk.Button(root, text=symbol, padx=20, pady=20, command=button_cos)
    elif symbol == 'tan':
        button = tk.Button(root, text=symbol, padx=20, pady=20, command=button_tan)
    elif symbol == 'log':
        button = tk.Button(root, text=symbol, padx=20, pady=20, command=button_log)
    elif symbol == 'ln':
        button = tk.Button(root, text=symbol, padx=20, pady=20, command=button_ln)
    elif symbol == '^':
        button = tk.Button(root, text=symbol, padx=20, pady=20, command=lambda: button_click('**'))
    elif symbol == '√':
        button = tk.Button(root, text=symbol, padx=20, pady=20, command=lambda: button_click('math.sqrt('))
    
    button.grid(row=grid_pos[0], column=grid_pos[1])

button_clear = tk.Button(root, text="C", padx=20, pady=20, command=button_clear)
button_clear.grid(row=5, column=2)

button_equal = tk.Button(root, text="=", padx=20, pady=20, command=button_equal)
button_equal.grid(row=5, column=4, columnspan=2)

root.mainloop()
