# IMPORT ALL THE NECESSARY MODULES

import tkinter as tk
from tkinter import messagebox as msgbox

#define the function to perform the calculations

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError #avoid the error when a numsgboxer is divided by 0
            result = num1 / num2
        elif operation == '**':
            result = num1 ** num2
        elif operation == '//':
            if num2 == 0:
                raise ZeroDivisionError #avoid the error when a numsgboxer is divided by 0
            result = num1 // num2
        elif operation == '%':
            if num2 == 0:
                raise ZeroDivisionError #avoid the error when a numsgboxer is divided by 0
            result = num1 % num2
        else:
            msgbox.showerror("Error", "Invalid operation selected") 
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        msgbox.showerror("Input Error", "Please enter valid numsgboxers") #check if valid numsgboxers are entered or not 
    except ZeroDivisionError:
        msgbox.showerror("Math Error", "Division by zero is not allowed") #avoid the error when a numsgboxer is divided by 0

# GUI setup

root = tk.Tk()
root.title("SIMPLE CALCULATOR")
root.geometry("600x600")
root.config(bg="#DDF981")

#Input numsgboxers

tk.Label(root, text="ENTER FIRST NUMBER:",font=("helvetica",15), bg="#bc76ea", fg="black", width=25).grid(row=0, column=0)
entry_num1 = tk.Entry(root,font=("helvetica",15), bg="#a2f3d4", fg="black", width=25)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="ENTER SECOND NUMBER:",font=("helvetica",15), bg="#bc76ea", fg="black", width=25).grid(row=1, column=0)
entry_num2 = tk.Entry(root,font=("helvetica",15), bg="#a2f3d4", fg="black", width=25)
entry_num2.grid(row=1, column=1)

tk.Label(root, text="CHOOSE:",font=("helvetica",15), bg="#0df337", fg="black", width=15).grid(row=2, column=0)

# Operation dropdown

operator = tk.StringVar()
operator.set('+')  # default value
operations = ['+', '-', '*', '/', '**', '//', '%']
tk.OptionMenu(root, operator, *operations).grid(row=2, column=1)
tk.Button(root, text="CALCULATE",font=("helvetica",15), bg="#f0874f", fg="black", width=15, command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

#Display Result 

result_label = tk.Label(root, text="RESULT: ",font=("helvetica",15), bg="#81d4f2", fg="black", width=40)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
