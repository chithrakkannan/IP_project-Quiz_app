import tkinter as tk
from login_system import sign_in, sign_up, admin_login

def main():
    darkgreen = '#298f29'
    root = tk.Tk()
    root.title("Quiz Application")
    root.geometry("900x600")
    root.configure(bg=darkgreen)
    root.resizable(False, False)

    welcome_label = tk.Label(root, text="Welcome !", font=("Arial", 45), bg=darkgreen, fg='white')
    welcome_label.place(x=325, y=130)

    inst_label = tk.Label(root, text="Kindly Sign in or Sign up to continue", font=("Arial", 18), bg=darkgreen, fg='white')
    inst_label.place(x=270, y=250)

    sign_in_button = tk.Button(root, text="Sign In", command=lambda: sign_in(root), font=("Arial", 16))
    sign_in_button.place(x=350, y=380)

    sign_up_button = tk.Button(root, text="Sign Up", command=lambda: sign_up(root), font=("Arial", 16))
    sign_up_button.place(x=500, y=380)

    admin_button = tk.Button(root, text="Admin ?", command=lambda: admin_login(root), font=("Arial", 10))
    admin_button.place(x=820, y=10)

    root.mainloop()

if __name__ == "__main__":
    main()
