def hello():
    print("jelloow")

hello()


my_list = [1,2,3]


my_list.appent()



import tkinter as tk
import re


login_pattern = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
CORRECT_PASSWORD = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")

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




def test_results():
    # Виведення назви програми
    print("Система результатів тестування")

    # Ініціалізація змінних
    total_students = 0
    passed_students = 0
    failed_students = 0

    while True:
        result = input("Введіть 'pass' для пройденого, 'fail' для невдалого або 'end' для зупинки: ")


        if result == "end":
            break


        if result == "pass":
            passed_students += 1
            total_students += 1
        elif result == "fail":
            failed_students += 1
            total_students += 1
        else:

            print("Невірний вхід, повторіть спробу!")


    print("Усього студентів:", total_students)
    print("Здано студентів:", passed_students)
    print("Студенти, які не склали:", failed_students)


    success_rate = (passed_students / total_students * 100) if total_students > 0 else 0
    print("Відсоток успішності:", success_rate, "%")


test_results()
















































































