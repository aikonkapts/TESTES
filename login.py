import tkinter as tk
from tkinter import messagebox


def try_login():
    username = entry_user.get()
    password = entry_pass.get()
    if username == "aikon" and password == "aikon":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid credentials")


def main():
    root = tk.Tk()
    root.title("Login")

    tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5)

    global entry_user, entry_pass
    entry_user = tk.Entry(root)
    entry_pass = tk.Entry(root, show="*")

    entry_user.grid(row=0, column=1, padx=5, pady=5)
    entry_pass.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(root, text="Login", command=try_login).grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
