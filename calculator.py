import tkinter as tk

# Function to perform the calculation
def calculate():
    try:
        result = eval(expression.get())
        expression.set(str(result))
    except Exception as e:
        expression.set("Error")

# Function to handle button click events
def button_click(value):
    current_expression = expression.get()
    new_expression = current_expression + str(value) 
    expression.set(new_expression)

# Function to all clear the expression
def all_clear_expression():
    expression.set("")

# Function for delete expression
def delete_last_character():
    current_expression = expression.get()
    new_expression = current_expression[:-1]
    expression.set(new_expression)   

# Function for decimal point
def add_decimal_point():
    current_expression = expression.get()
    if current_expression and current_expression[-1].isdigit():
        new_expression = current_expression + "."
        expression.set(new_expression)

# The main window
window = tk.Tk()
window.title("CALCULATOR")
window.configure(bg="black")

# expression variable
expression = tk.StringVar()
expression.set("")

# Create the entry widget to display the expression
entry = tk.Entry(window, textvariable=expression, justify="right")
entry.grid(row=0, column=0, columnspan=10, padx=10, pady=10)
entry.configure(fg="black", bg="white",font=("Arial", 14,"bold" ))

# Buttons for numbers
for i in range(1, 10):
    button = tk.Button(window, text=str(i), width=10, command=lambda num=i: button_click(num))
    button.grid(row=(i-1) // 3 + 1, column=(i-1) % 3, padx=2, pady=2)
    button.configure(fg="black" ,bg="darkgray", font=("Arial", 12,"bold" ))

# Button for Zero
zero_button = tk.Button(window,text="0", width="10",command=lambda: button_click(0))
zero_button.grid(row=4,column=1,padx=5,pady=5)
zero_button.configure(fg="black" ,bg="darkgray", font=("Arial", 12,"bold" ))

# Buttons for operators
operators = ['+', '-', '*', '/']
for i in range(len(operators)):
    button = tk.Button(window, text=operators[i], width=10, command=lambda op=operators[i]: button_click(op))
    button.grid(row=i+1, column=3, padx=5, pady=5)
    button.configure(fg="black" ,bg="orangered", font=("Arial", 12,"bold" ))
# Decimal point button
decimal_point = tk.Button(window, text=".", width=10, command=add_decimal_point)
decimal_point.grid(row=4, column=0, padx=5, pady=5)
decimal_point.configure(fg="black" ,bg="orangered", font=("Arial", 12,"bold" ))

# Equals '=' button
equals_button = tk.Button(window, text="=", width=10, command=calculate)
equals_button.grid(row=4, column=2, padx=5, pady=5)
equals_button.configure(fg="black" ,bg="orangered", font=("Arial", 12,"bold" ))

# Delete bButton
delete_button = tk.Button(window, text="del", width=10, command=delete_last_character)
delete_button.grid(row=0, column=3, padx=5, pady=5)
delete_button.configure(fg="white" ,bg="darkblue", font=("Arial", 12,"bold" ))

# All Clear button
all_clear_button = tk.Button(window, text="AC", width=10, command=all_clear_expression)
all_clear_button.grid(row=0, column=0, padx=5, pady=5)
all_clear_button.configure(fg="white" ,bg="darkblue", font=("Arial", 12,"bold" ))

# Start the main loop
window.mainloop()
