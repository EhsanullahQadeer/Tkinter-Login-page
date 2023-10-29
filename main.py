import tkinter as tk
from tkinter import messagebox

def login():
    email = email_entry.get()
    roll_no = roll_no_entry.get()
    password = password_entry.get()

    # You can replace these with your authentication logic
    if email == "user@example.com" and password == "password":
        messagebox.showinfo("Login Successful", f"Welcome, {roll_no}!")
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")

# Create the main window
root = tk.Tk()
root.title("Beautiful Login Page")

# Customize window size and background color
root.geometry("400x400")
root.configure(bg="#f1f1f1")

# Create and place widgets
frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.pack(pady=50)

title_label = tk.Label(frame, text="Login Page", font=("Helvetica", 20), bg="#ffffff")
title_label.grid(row=0, column=1, pady=(0, 20))

email_label = tk.Label(frame, text="Email:", font=("Helvetica", 12), bg="#ffffff")
email_label.grid(row=1, column=0)
email_entry = tk.Entry(frame, font=("Helvetica", 12)
)
email_entry.insert(0, "user@example.com")  # Set default email
email_entry.grid(row=1, column=1)

roll_no_label = tk.Label(frame, text="Roll No:", font=("Helvetica", 12), bg="#ffffff")
roll_no_label.grid(row=2, column=0)
roll_no_entry = tk.Entry(frame, font=("Helvetica", 12))
roll_no_entry.insert(0, "Your Roll No")  # Set default roll number
roll_no_entry.grid(row=2, column=1)

password_label = tk.Label(frame, text="Password:", font=("Helvetica", 12), bg="#ffffff")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(frame, show="*", font=("Helvetica", 12))
password_entry.insert(0, "password")  # Set default password
password_entry.grid(row=3, column=1)

login_button = tk.Button(frame, text="Login", command=login, font=("Helvetica", 12), bg="#4CAF50", fg="white")
login_button.grid(row=4, column=1, pady=20)

# Start the main loop
root.mainloop()
