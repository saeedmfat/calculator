# Import necessary libraries
import tkinter as tk  # Import Tkinter for GUI
import math  # Import math for scientific calculations

# Create the main window for the calculator
root = tk.Tk()
root.title("Calculator")  # Set the title of the window

# Function to evaluate the expression entered by the user
def evaluate_expression():
    try:
        expression = entry.get()  # Get the expression from the entry widget
        result = str(eval(expression))  # Evaluate the expression using eval()
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(tk.END, result)  # Insert the result into the entry widget
        add_to_history(expression + " = " + result)  # Add the expression to history
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the entry if there's an error
        entry.insert(tk.END, "Error")  # Display "Error" if evaluation fails

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)  # Delete all content in the entry widget

# Function to toggle between light and dark themes
def toggle_theme():
    if theme.get() == "light":  # Check the current theme
        root.config(bg='#2c2c2c')  # Change window background to dark
        entry.config(bg='#333333', fg='white')  # Change entry widget to dark theme
        for button in buttons:
            button.config(bg='#444444', fg='white', activebackground='#555555', activeforeground='white')  # Update button colors
        theme.set("dark")  # Set the theme to dark
    else:
        root.config(bg='#f0f0f0')  # Change window background to light
        entry.config(bg='#ffffff', fg='black')  # Change entry widget to light theme
        for button in buttons:
            button.config(bg='#e1e1e1', fg='black', activebackground='#d3d3d3', activeforeground='black')  # Update button colors
        theme.set("light")  # Set the theme to light

# Function to add the calculation to the history list
def add_to_history(entry_text):
    history_list.insert(tk.END, entry_text)  # Insert the text at the end of the history list
    history_list.yview(tk.END)  # Scroll the history list to the bottom to show the latest entry

# Function to clear the history list
def clear_history():
    history_list.delete(0, tk.END)  # Delete all history entries

# Function to handle keypress events for keyboard input
def handle_keypress(event):
    # Check if the key pressed is a number or an operator
    if event.char.isdigit() or event.char in "+-*/.=":
        current_text = entry.get()  # Get the current content in the entry widget
        if current_text and event.char == current_text[-1]:  # If the last character is the same as the pressed key, do nothing
            return
        entry.insert(tk.END, event.char)  # Insert the pressed character into the entry widget
    elif event.keysym == "BackSpace":  # If the backspace key is pressed
        entry.delete(len(entry.get())-1, tk.END)  # Delete the last character from the entry widget
    elif event.keysym == "Return":  # If the Enter (Return) key is pressed
        evaluate_expression()  # Evaluate the expression in the entry widget


# Function to perform scientific functions
def scientific_function(func):
    try:
        expr = entry.get()  # Get the current expression from the entry widget
        if func == "sin":  # If the function is 'sin'
            result = str(math.sin(math.radians(float(expr))))  # Calculate sine of the angle (converted to radians)
        elif func == "cos":  # If the function is 'cos'
            result = str(math.cos(math.radians(float(expr))))  # Calculate cosine of the angle (converted to radians)
        elif func == "sqrt":  # If the function is 'sqrt' (square root)
            result = str(math.sqrt(float(expr)))  # Calculate the square root
        elif func == "log":  # If the function is 'log' (logarithm base 10)
            result = str(math.log(float(expr), 10))  # Calculate the base-10 logarithm
        
        # Round the result to avoid floating-point precision issues
        result = str(round(float(result), 8))  # Round the result to 8 decimal places
        
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(tk.END, result)  # Insert the result into the entry widget
        add_to_history(expr + " (" + func + ") = " + result)  # Add the result to the history
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the entry widget in case of error
        entry.insert(tk.END, "Error")  # Display "Error" if something goes wrong


# String variable to keep track of the theme (light or dark)
theme = tk.StringVar(value="light")

# Create the entry widget for input
entry = tk.Entry(root, width=20, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)  # Place the entry widget in the grid layout

# Create a label for the history section
history_label = tk.Label(root, text="History", font=("Arial", 12))
history_label.grid(row=0, column=4)  # Place the label in the grid

# Create a listbox for showing the history of calculations
history_list = tk.Listbox(root, height=10, width=30, font=("Arial", 12))
history_list.grid(row=1, column=4, rowspan=5)  # Place the listbox in the grid

# Define the button labels and their positions in the grid
buttons_info = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('change', 5, 1),
    ('sin', 6, 0), ('cos', 6, 1), ('sqrt', 6, 2), ('log', 6, 3)
]

# Create a list to hold the button references
buttons = []

# Create the buttons based on the button information
for (text, row, col) in buttons_info:
    if text == 'C':  # If the button is 'C', it clears the entry
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=clear_entry)
    elif text == 'change':  # If the button is 'change', it toggles the theme
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=toggle_theme)
    elif text in ["sin", "cos", "sqrt", "log"]:  # If the button is a scientific function
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=lambda t=text: scientific_function(t))
    else:  # For all other buttons (numbers and operators)
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=lambda t=text: entry.insert(tk.END, t) if t != "=" else evaluate_expression())
    
    button.grid(row=row, column=col, padx=5, pady=5)  # Place the button in the grid
    buttons.append(button)  # Add the button to the list of buttons

# Apply the initial theme (light theme)
toggle_theme()

# Bind keyboard key events to the handle_keypress function
root.bind("<Key>", handle_keypress)

# Start the Tkinter event loop to make the GUI interactive
root.mainloop()


