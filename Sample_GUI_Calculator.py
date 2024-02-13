import tkinter as tk
import math

# Function to update the display when a button is clicked
def on_button_click(value):
    current = display.get()
    if value == 'C':
        display.delete(0, tk.END)
    elif value == '=':
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == 'sqrt':
        try:
            result = math.sqrt(float(current))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == 'cbrt':
        try:
            result = round(float(current) ** (1 / 3), 10)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == '|x|':
        try:
            result = abs(float(current))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == 'x^2':
        try:
            result = round(float(current) ** 2, 10)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == 'x^3':
        try:
            result = round(float(current) ** 3, 10)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == 'sin':
        try:
            result = math.sin(math.radians(float(current)))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == 'cos':
        try:
            result = math.cos(math.radians(float(current)))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == 'tan':
        try:
            result = math.tan(math.radians(float(current)))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, value)

# Create the main window
root = tk.Tk()
root.title("Enhanced Calculator")

# Create the display
display = tk.Entry(root, width=25, font=('Arial', 14), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    '|x|', 'x^2', 'sqrt', 'x^3', 'cbrt',
    'sin', 'cos', 'tan'
]

# Create buttons and place them in the window
row_val = 1
col_val = 0

for label in button_labels:
    if label != '=':
        tk.Button(root, text=label, width=5, command=lambda x=label: on_button_click(x)).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=label, width=5, command=lambda x=label: on_button_click(x)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
