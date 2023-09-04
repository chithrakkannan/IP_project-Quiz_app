import tkinter as tk
from tkinter import messagebox

def sign_in(root):
    sign_in_window = tk.Toplevel(root)
    sign_in_window.title("Sign In")
    sign_in_window.geometry("400x200")
    sign_in_window.configure(bg='#8ABD5E')
    sign_in_window.resizable(False, False)

    sign_in_username_label = tk.Label(sign_in_window, text="Username:")
    sign_in_username_label.grid(row=0, column=0, padx=80, pady=40)
    sign_in_username_entry = tk.Entry(sign_in_window)
    sign_in_username_entry.grid(row=0, column=1, padx=5, pady=40)

    sign_in_password_label = tk.Label(sign_in_window, text="Password:")
    sign_in_password_label.grid(row=1, column=0, padx=80, pady=5)
    sign_in_password_entry = tk.Entry(sign_in_window, show="*")
    sign_in_password_entry.grid(row=1, column=1, padx=5, pady=5)

    def handle_sign_in():
        username = sign_in_username_entry.get()
        password = sign_in_password_entry.get()

        if username == "username" and password == "password":
            messagebox.showinfo("Sign In", "Sign In Successful!")
            sign_in_window.destroy()
        else:
            messagebox.showerror("Sign In", "Invalid Username or Password")

    sign_in_button = tk.Button(sign_in_window, text="Sign In", command=handle_sign_in)
    sign_in_button.grid(row=2, columnspan=2, pady=20, padx=80)

def sign_up(root):
    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("900x500")
    sign_up_window.configure(bg='#8ABD5E')
    sign_up_window.resizable(False, False)

    sign_up_name_label = tk.Label(sign_up_window, text="Name:")
    sign_up_name_label.grid(row=0, column=0, padx=80, pady=40)
    sign_up_name_entry = tk.Entry(sign_up_window)
    sign_up_name_entry.grid(row=0, column=1, padx=5, pady=40)

    sign_up_dob_label = tk.Label(sign_up_window, text="Date of Birth (YYYY-MM-DD):")
    sign_up_dob_label.grid(row=1, column=0, padx=80, pady=10)
    sign_up_dob_entry = tk.Entry(sign_up_window)
    sign_up_dob_entry.grid(row=1, column=1, padx=5, pady=10)

    sign_up_sex_label = tk.Label(sign_up_window, text="Gender:")
    sign_up_sex_label.grid(row=2, column=0, padx=80, pady=10)
    sign_up_sex_entry = tk.Entry(sign_up_window)
    sign_up_sex_entry.grid(row=2, column=1, padx=5, pady=10)

    sign_up_email_label = tk.Label(sign_up_window, text="Email:")
    sign_up_email_label.grid(row=3, column=0, padx=80, pady=10)
    sign_up_email_entry = tk.Entry(sign_up_window)
    sign_up_email_entry.grid(row=3, column=1, padx=5, pady=10)

    sign_up_username_label = tk.Label(sign_up_window, text="Username:")
    sign_up_username_label.grid(row=4, column=0, padx=80, pady=10)
    sign_up_username_entry = tk.Entry(sign_up_window)
    sign_up_username_entry.grid(row=4, column=1, padx=5, pady=10)

    sign_up_password_label = tk.Label(sign_up_window, text="Password:")
    sign_up_password_label.grid(row=5, column=0, padx=80, pady=10)
    sign_up_password_entry = tk.Entry(sign_up_window, show="*")
    sign_up_password_entry.grid(row=5, column=1, padx=5, pady=10)

    def handle_sign_up():
        t_username = sign_up_username_entry.get()
        t_password = sign_up_password_entry.get()

        if t_username == "username" and t_password == "password":
            messagebox.showerror("Sign Up", "Username already exist")

        else:
            messagebox.showinfo("Sign Up", "Sign In Successful!, Now Sign in with your Account")
            sign_up_window.destroy()


    sign_up_button = tk.Button(sign_up_window, text="Sign Up", command=handle_sign_up)
    sign_up_button.grid(row=6, columnspan=2, pady=20, padx=100)

def admin_login(root):  # Pass 'root' as an argument
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Login")
    admin_window.geometry("380x180")
    admin_window.configure(bg='#404040')
    admin_window.resizable(False, False)

    admin_username_label = tk.Label(admin_window, text="Username:")
    admin_username_label.grid(row=0, column=0, padx=80, pady=40)
    admin_username_entry = tk.Entry(admin_window)
    admin_username_entry.grid(row=0, column=1, padx=5, pady=40)

    admin_password_label = tk.Label(admin_window, text="Password:")
    admin_password_label.grid(row=1, column=0, padx=80, pady=5)
    admin_password_entry = tk.Entry(admin_window, show="*")
    admin_password_entry.grid(row=1, column=1, padx=5, pady=5)

    def handle_admin_login():
        username = admin_username_entry.get()
        password = admin_password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Sign In", "Sign In Successful!")
            admin_window.destroy()
        else:
            messagebox.showerror("Sign In", "Invalid Username or Password")

    admin_login_button = tk.Button(admin_window, text="Sign In", command=handle_admin_login)
    admin_login_button.grid(row=2, columnspan=2, pady=20, padx=80)

if __name__ == "__main__":
    root = tk.Tk()
    admin_login(root)  # Call the function with 'root' as an argument for testing
    root.mainloop()