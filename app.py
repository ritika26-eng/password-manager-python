import tkinter as tk
from tkinter import messagebox

import database
from encryption import encrypt

database.init_db()

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")


def save():
    site = e1.get()
    user = e2.get()
    pwd = e3.get()

    if not site or not user or not pwd:
        messagebox.showerror("Error", "All fields required")
        return

    encrypted = encrypt(pwd)
    database.add_password(site, user, encrypted)

    messagebox.showinfo("Success", "Saved!")

    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)


tk.Label(root, text="Website").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Username").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Password").pack()
e3 = tk.Entry(root, show="*")
e3.pack()

tk.Button(root, text="Save", command=save).pack(pady=10)

root.mainloop()