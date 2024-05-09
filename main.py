#Dmitrii Gusev
import tkinter as tk
from tkinter import messagebox
import math


def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # calculating discriminant
        discriminant = b ** 2 - 4 * a * c

        #checking if the discriminant equal to positive, negative number or zero
        if discriminant > 0:
            # Two real and different roots
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            messagebox.showinfo("Roots", f"Roots: {root1}, {root2}")
        elif discriminant == 0:
            # One real root
            root = -b / (2 * a)
            messagebox.showinfo("Root", f"Root: {root}")
        else:
            # roots with imaginary numbers
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            messagebox.showinfo("Roots", f"Roots: {root1}, {root2}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")


#creating a tkinter window
root = tk.Tk()
root.title("Quadratic Equation Solver")

# Create input fields for coefficients (a,b,c)
label_a = tk.Label(root, text="Enter coefficient a:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

label_b = tk.Label(root, text="Enter coefficient b:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

label_c = tk.Label(root, text="Enter coefficient c:")
label_c.grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

#create a button to solve the equation
solve_button = tk.Button(root, text="Solve", command=solve_quadratic)
solve_button.grid(row=3, columnspan=2)

#start the tkinter event loop
root.mainloop()
