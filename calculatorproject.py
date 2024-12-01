import customtkinter
from tkinter import END
END='end'
print(END)
# Function to evaluate the expression and display the result
def answer():
    try:
        expression = entryField.get()  # Get the expression from the entry field
        # Replace the division sign '÷' with the Python division operator '/'
        expression = expression.replace('÷', '/')
        result = eval(expression)  # Evaluate the expression
        entryField.delete(0, END)  # Clear the entry field
        entryField.insert(END, str(result))  # Insert the result back into the entry field
    except ZeroDivisionError:
        entryField.delete(0, END)  # Clear the entry field in case of division by zero
        entryField.insert(END, "Can't divide by zero")  # Display error message
    except Exception as e:
        entryField.delete(0, END)  # Clear the entry field in case of other errors
        entryField.insert(END, "Error")  # Display error message

# Function to insert numbers and operators into the entry field
def click(number):
    current = entryField.get()
    entryField.delete(0, END)
    entryField.insert(END, current + number)

# Function to clear the entry field
def clear():
    entryField.delete(0, END)

# Create the root window
root = customtkinter.CTk()
root.title("Calculator")
root.geometry("300x320")
root.config(bg="black")

# Create the entry field
entryField = customtkinter.CTkEntry(root, font=("arial", 20, "bold"),
                                    text_color="white", fg_color="black",
                                    border_color="white", width=280, height=50, bg_color="black")
entryField.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

# Create buttons for the calculator
b7 = customtkinter.CTkButton(root, text="7", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("7"))
b7.grid(row=1, column=0, pady=10)
b8 = customtkinter.CTkButton(root, text="8", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("8"))
b8.grid(row=1, column=1)
b9 = customtkinter.CTkButton(root, text="9", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("9"))
b9.grid(row=1, column=2)
bplus = customtkinter.CTkButton(root, text="+", width=60, text_color="white", fg_color="orange", cursor='hand2', command=lambda: click("+"))
bplus.grid(row=1, column=3, padx=10, pady=10)

b4 = customtkinter.CTkButton(root, text="4", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("4"))
b4.grid(row=2, column=0, pady=10)
b5 = customtkinter.CTkButton(root, text="5", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("5"))
b5.grid(row=2, column=1)
b6 = customtkinter.CTkButton(root, text="6", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("6"))
b6.grid(row=2, column=2)
bminus = customtkinter.CTkButton(root, text="-", width=60, text_color="white", fg_color="orange", cursor='hand2', command=lambda: click("-"))
bminus.grid(row=2, column=3)

b1 = customtkinter.CTkButton(root, text="1", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("1"))
b1.grid(row=3, column=0, pady=10)
b2 = customtkinter.CTkButton(root, text="2", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("2"))
b2.grid(row=3, column=1)
b3 = customtkinter.CTkButton(root, text="3", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("3"))
b3.grid(row=3, column=2)
bmultiply = customtkinter.CTkButton(root, text="*", width=60, text_color="white", fg_color="orange", cursor='hand2', command=lambda: click("*"))
bmultiply.grid(row=3, column=3)

b0 = customtkinter.CTkButton(root, text="0", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("0"))
b0.grid(row=4, column=0, pady=10)
bdot = customtkinter.CTkButton(root, text=".", width=60, text_color="white", fg_color="blue", cursor='hand2', command=lambda: click("."))
bdot.grid(row=4, column=1)
bclear = customtkinter.CTkButton(root, text="C", width=60, text_color="white", fg_color="red", hover_color='red4', command=clear)
bclear.grid(row=4, column=2)
bdivision = customtkinter.CTkButton(root, text="÷", width=60, text_color="white", fg_color="orange", hover_color='orange3', command=lambda: click("÷"))
bdivision.grid(row=4, column=3)

# Equal button to evaluate the expression
bequal = customtkinter.CTkButton(root, text="=", width=280, text_color="white", fg_color="green", hover_color='dark green', command=answer)
bequal.grid(row=5, column=0, columnspan=4, pady=10)

# Start the main event loop
root.mainloop()
