import customtkinter
from tkinter import messagebox
import functions

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create a new Tkinter window
root = customtkinter.CTk()
root.geometry("385x385")
root.title("Gas Cost Calculator")

# Define a validation function to restrict user input to numbers only
def validate_number(input):
    if input.isdigit() or input == ".":
        return True
    try:
        float(input)
        return True
    except ValueError:
        return False

# Create a frame to hold the input elements
input_frame = customtkinter.CTkFrame(root)
input_frame.pack(padx=20, pady= 20, fill="both", expand=True)

# Create labels and entry boxes for user input
distance1_label = customtkinter.CTkLabel(master=input_frame, text="Distance to gas station 1:")
distance1_label.grid(row=0, column=0, padx=10,pady=10)
distance1_entry = customtkinter.CTkEntry(input_frame, validate="key", validatecommand=(root.register(validate_number), "%S"))
distance1_entry.grid(row=0, column=1, padx=10,pady=10)

cost1_label = customtkinter.CTkLabel(master=input_frame, text="Cost of gas at gas station 1:")
cost1_label.grid(row=1, column=0, padx=10,pady=10)
cost1_entry = customtkinter.CTkEntry(master=input_frame, validate="key", validatecommand=(root.register(validate_number), "%S"))
cost1_entry.grid(row=1, column=1, padx=10,pady=10)

distance2_label = customtkinter.CTkLabel(master=input_frame, text="Distance to gas station 2:")
distance2_label.grid(row=2, column=0, padx=10,pady=10)
distance2_entry = customtkinter.CTkEntry(master=input_frame, validate="key", validatecommand=(root.register(validate_number), "%S"))
distance2_entry.grid(row=2, column=1, padx=10,pady=10)

cost2_label = customtkinter.CTkLabel(master=input_frame, text="Cost of gas at gas station 2:")
cost2_label.grid(row=3, column=0, padx=10,pady=10)
cost2_entry = customtkinter.CTkEntry(master=input_frame, validate="key", validatecommand=(root.register(validate_number), "%S"))
cost2_entry.grid(row=3, column=1, padx=10,pady=10)

mpg_label = customtkinter.CTkLabel(master=input_frame, text="Vehicle MPG:")
mpg_label.grid(row=4, column=0, padx=10,pady=10)
mpg_entry = customtkinter.CTkEntry(master=input_frame, validate="key", validatecommand=(root.register(validate_number), "%S"))
mpg_entry.grid(row=4, column=1, padx=10,pady=10)

gallons_label = customtkinter.CTkLabel(master=input_frame, text="Gallons to fill:")
gallons_label.grid(row=5, column=0, padx=10,pady=10)
gallons_entry = customtkinter.CTkEntry(master=input_frame, placeholder_text="avg sedan 18, large pickup 35", validate="key", validatecommand=(root.register(validate_number), "%S"))
gallons_entry.grid(row=5, column=1, padx=10,pady=10)

def clear_entries():
    distance1_entry.delete(0, customtkinter.END)
    distance2_entry.delete(0, customtkinter.END)
    cost1_entry.delete(0, customtkinter.END)
    cost2_entry.delete(0, customtkinter.END)
    mpg_entry.delete(0, customtkinter.END)
    gallons_entry.delete(0, customtkinter.END)

clear_button = customtkinter.CTkButton(input_frame, text="Clear", command=clear_entries)
clear_button.grid(row=6, column=0, padx=10,pady=10)

# Create a function to calculate the gas cost when the button is clicked
def calculate_gas_cost():
    try:
        distance1 = float(distance1_entry.get())
        distance2 = float(distance2_entry.get())
        cost1 = float(cost1_entry.get())
        cost2 = float(cost2_entry.get())
        mpg = float(mpg_entry.get())
        gallons = float(gallons_entry.get())

        # Calculate the gas cost using the user input and the functions module
        result = functions.calculate_cost(distance1, distance2, cost1, cost2, mpg, gallons)

        # Display the result in a message box
        messagebox.showinfo("Gas Cost Calculator", result)

    except ValueError:
        # If any of the user inputs are not valid numbers, display an error message
        messagebox.showerror("Error", "Please enter valid numbers for all input fields.")

# Create a button to calculate the gas cost
calculate_button = customtkinter.CTkButton(input_frame, text="Calculate", command=calculate_gas_cost)
calculate_button.grid(row=6, column=1, padx=10,pady=10)


# Run the Tkinter event loop
root.mainloop()
