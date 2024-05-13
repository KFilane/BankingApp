import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle login button click event
def login():
    password = generate_password()
    messagebox.showinfo("Login Password", f"Your login password is: {password}")

# Create the main window
root = tk.Tk()
root.title("Bank Application")

# Create a label
label = tk.Label(root, text="Welcome to the Bank Application!", font=("Helvetica", 16))
label.pack(pady=10)

# Create a login button
login_button = tk.Button(root, text="Generate Login Password", command=login)
login_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
