import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = entry_length.get()
    
    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number!")
        return
    
    length = int(length)
    if length < 6:
        messagebox.showwarning("Warning", "Password too short! Choose at least 6 characters.")
        return
    
    # Build the character pool based on user choices
    char_pool = ""
    if var_upper.get(): char_pool += string.ascii_uppercase
    if var_lower.get(): char_pool += string.ascii_lowercase
    if var_digits.get(): char_pool += string.digits
    if var_symbols.get(): char_pool += string.punctuation
    
    if not char_pool:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    
    # Update password strength
    update_strength(password)

# Function to update password strength
def update_strength(password):
    strength = "Weak"
    if len(password) >= 12 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"
    
    strength_label.config(text=f"Password Strength: {strength}")
    if strength == "Weak":
        strength_label.config(fg="#e74c3c")  # Red
    elif strength == "Medium":
        strength_label.config(fg="#f1c40f")  # Yellow
    else:
        strength_label.config(fg="#2ecc71")  # Green

# Function to copy password to clipboard
def copy_password():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main Window
root = tk.Tk()
root.title("✨ Advanced Password Generator ✨")

# ✅ Make window full screen
root.state("zoomed")  # Works on Windows (maximizes the window)
# root.attributes('-fullscreen', True)  # Uncomment this for true full-screen (no window borders)

root.config(bg="#2c3e50")

# Title Label
title_label = tk.Label(root, text="🔐 Advanced Password Generator 🔐", font=("Poppins", 28, "bold"), fg="#ffffff", bg="#2c3e50")
title_label.pack(pady=40)

# Password Length Frame
frame_length = tk.Frame(root, bg="#2c3e50")
frame_length.pack(pady=10)

length_label = tk.Label(frame_length, text="Password Length: ", font=("Poppins", 18), fg="#ecf0f1", bg="#2c3e50")
length_label.pack(side=tk.LEFT, padx=10)

entry_length = tk.Entry(frame_length, font=("Poppins", 18), width=5, justify="center")
entry_length.pack(side=tk.LEFT, padx=10)
entry_length.insert(0, "12")  # Default length

# Character type checkboxes
frame_options = tk.Frame(root, bg="#2c3e50")
frame_options.pack(pady=15)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(frame_options, text="Uppercase", font=("Poppins", 16), variable=var_upper, bg="#2c3e50", fg="#ecf0f1", selectcolor="#34495e").pack(side=tk.LEFT, padx=20)
tk.Checkbutton(frame_options, text="Lowercase", font=("Poppins", 16), variable=var_lower, bg="#2c3e50", fg="#ecf0f1", selectcolor="#34495e").pack(side=tk.LEFT, padx=20)
tk.Checkbutton(frame_options, text="Numbers", font=("Poppins", 16), variable=var_digits, bg="#2c3e50", fg="#ecf0f1", selectcolor="#34495e").pack(side=tk.LEFT, padx=20)
tk.Checkbutton(frame_options, text="Symbols", font=("Poppins", 16), variable=var_symbols, bg="#2c3e50", fg="#ecf0f1", selectcolor="#34495e").pack(side=tk.LEFT, padx=20)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", font=("Poppins", 18, "bold"), bg="#27ae60", fg="#ffffff",
                         activebackground="#2ecc71", activeforeground="#ffffff", command=generate_password)
generate_btn.pack(pady=25, ipadx=15, ipady=8)

# Password Display
entry_password = tk.Entry(root, font=("Poppins", 20, "bold"), width=45, justify="center", bd=2, relief="solid")
entry_password.pack(pady=20)

# Password Strength Label
strength_label = tk.Label(root, text="Password Strength: ", font=("Poppins", 18, "bold"), fg="#ffffff", bg="#2c3e50")
strength_label.pack(pady=10)

# Copy Button
copy_btn = tk.Button(root, text="Copy Password", font=("Poppins", 18, "bold"), bg="#2980b9", fg="#ffffff",
                     activebackground="#3498db", activeforeground="#ffffff", command=copy_password)
copy_btn.pack(pady=20, ipadx=15, ipady=8)

# Footer
footer = tk.Label(root, text="✨ Designed by Kriti Sharma", font=("Poppins", 10), bg="#3A6F82", fg="white")
footer.pack(side="bottom", pady=10)

# Run the app
root.mainloop()
