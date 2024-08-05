import random
import string
from tkinter import *

# Function to generate the password
def generate_password():
    try:
        pass_length = int(length_entry.get())
        if pass_length <= 0:
            result_label.config(text="Please enter a positive length.")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    values = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(values) for _ in range(pass_length))
    result.config(text=f"Your random password is: {password}")

# Create the main window
win= Tk()
win.title("Password Generator")
win.geometry("400x400")
win.configure(bg="#1E90FF")  

# Length input label and entry
length = Label(win, text="Enter password length:", bg="#e0f7fa", font=("Helvetica", 12))
length.pack(pady=10)

length_entry = Entry(win, font=("Helvetica", 12))
length_entry.pack(pady=5)

# Generate button
generate_button = Button(win, text="Generate Password", command=generate_password, bg="#FF8DAA", fg="white", font=("Helvetica", 12))
generate_button.pack(pady=15)

# Result label
result = Label(win, text="", bg="#e0f7fa", font=("Helvetica", 12))
result.pack(pady=10)

# Run the application
win.mainloop()