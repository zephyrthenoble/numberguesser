import tkinter as tk

def check_values():
    # Get the values from the text boxes
    values = [textbox.get() for textbox in textboxes]

    # Calculate the first 6 numbers in the Fibonacci sequence
    fib1 = 2
    fib2 = 3
    fib3 = fib1 + fib2
    fib4 = fib2 + fib3
    fib5 = fib3 + fib4
    fib6 = fib4 + fib5

    # Check if the values are correct
    for i, (value, fib) in enumerate(zip(values, [fib1, fib2, fib3, fib4, fib5, fib6])):
        if value == str(fib):
            textboxes[i].config(bg="green")
        else:
            textboxes[i].config(bg="white")
    # Check if the values are correct
    if all(value == str(fib) for value, fib in zip(values, [fib1, fib2, fib3, fib4, fib5, fib6])):
        result_label.config(text="Success")
        lock_label.config(image=unlocked_image)
    else:
        result_label.config(text="Failure")

# Create the window
window = tk.Tk()
window.title("Start where 2 is 3")  # Add a title to the window

# Create the label above the text boxes
label = tk.Label(window, text="Unlock the function", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=6, pady=10)

# Create the text boxes
textboxes = [tk.Entry(window, width=5, font=("Arial", 16)) for _ in range(6)]


# Position the text boxes in a grid layout
for i, textbox in enumerate(textboxes):
    textbox.grid(row=1, column=i, padx=10, pady=10)
    textbox.insert(0, str(i))

# Create the lock icon label
locked_image = tk.PhotoImage(file="lock.png").subsample(5)  # Create a photo object from the locked lock image file and resize it to 20x20 pixels
unlocked_image = tk.PhotoImage(file="unlock.png").subsample(5)  # Create a photo object from the unlocked lock image file and resize it to 20x20 pixels
lock_label = tk.Label(window, image=locked_image)

# Create the button
button = tk.Button(window, text="Check Values", command=check_values)

# Create the result label
result_label = tk.Label(window, text="", font=("Arial", 16))

# Position the lock icon label, button, and result label in the grid layout
lock_label.grid(row=2, column=1, padx=10, pady=10)
button.grid(row=2, column=2, padx=10, pady=10)
result_label.grid(row=3, column=2, padx=10, pady=10)

# Start the main loop
window.mainloop()