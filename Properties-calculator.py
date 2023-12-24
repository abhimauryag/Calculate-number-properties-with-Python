import tkinter as tk

# Function to calculate the square and cube
def calculate(event=None):
    user_input = entry.get()
    try:
        number = int(user_input)
        square = number ** 2
        cube = number ** 3

        # Determine if the given number is a square of another number
        is_square = int(number ** 0.5) ** 2 == number
        square_root = int(number ** 0.5) if is_square else None

        # Determine if the given number is a cube of another number
        is_cube = int(number ** (1 / 3)) ** 3 == number
        cube_root = int(number ** (1 / 3)) if is_cube else None

        # Find factors of the given number
        factors = [i for i in range(1, number + 1) if number % i == 0]

        result_label.config(text=f"User Input: {number}\n"
                                 f"Is square of: {square_root}          "
                                 f"Is cube of: {cube_root}\n"
                                 f"Square: {square}           "
                                 f"Cube: {cube}\n"
                                 f"Factors: {factors}")
        entry.delete(0, 'end')  # Clear the input field
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Create the main application window
app = tk.Tk()
app.title("Properties of a Number")
app.geometry("400x300")  # Set the window size

# Create and configure the input entry field
entry_label = tk.Label(app, text="Enter a number:", font=("Arial", 14))
entry_label.pack(pady=10)
entry = tk.Entry(app, font=("Arial", 14), width=20)
entry.pack()
entry.focus_set()  # Set focus on the entry widget

# Bind the Enter key to the entry field
entry.bind("<Return>", calculate)

# Create a button to trigger the calculation
calculate_button = tk.Button(app, text="Check Properties", command=calculate, font=("Arial", 14))
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Arial", 16))
result_label.pack()

# Start the GUI main loop
app.mainloop()
