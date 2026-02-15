import tkinter as tk
import re

login_pattern = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
CORRECT_PASSWORD = re.compile(r"^\w(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")


def validate_credentials():
    login = username_entry.get()
    password = password_entry.get()

    if re.fullmatch(login_pattern, login) and re.fullmatch(CORRECT_PASSWORD, password):
        username_entry.config(bg="lightgreen")
        password_entry.config(bg="lightgreen")
    else:
        username_entry.config(bg="lightcoral")
        password_entry.config(bg="lightcoral")


root = tk.Tk()
root.title("Login Validation")
root.geometry("750x400")

username_label = tk.Label(root, text="Login:")
username_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

validate_button = tk.Button(root, text="Validate", command=validate_credentials)
validate_button.pack(pady=20)

root.mainloop()






login_pattern = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
login_pattern_hard = re.compile(r"[a-zA-Z0-9._%+-]{2,6}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,8}$")

login = input("enter email")

if login_pattern_hard.search(login):
    print("login is corect")

else:
    print("login isn't corect")


password_pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d{6,})")
password = input("enter password:")

if password_pattern.search(password):
    print("password is corect")

else:
    print("password isn't corect")


pasword = re.compile(r"^Nazar.{8,}$")


password = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")















































