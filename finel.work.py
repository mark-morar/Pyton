# 1 ЗАВДАННЯ
name = input("Введіть ім'я співробітника: ")
hourly_rate = float(input("Введіть ставку за годину: "))
hours_worked = int(input("Введіть кількість відпрацьованих годин: "))

gross_salary = hourly_rate * hours_worked
tax = gross_salary * 0.2
net_salary = gross_salary - tax

print(f"{name}, ваша зарплата після вирахування податку: {net_salary:.2f} грн")


# 2 ЗАВДАННЯ

def show_tasks(tasks):
   
    if not tasks:
        print("Список справ порожній!")
    else:
        print("\nСписок справ:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


tasks = input("Введіть список справ через кому: ").split(", ")
tasks = [task.strip() for task in tasks]

while True:
    show_tasks(tasks)

    action = input("Введіть номер справи для видалення або 'q' для виходу: ").strip()

    if action.lower() == 'q':
        print("Програму завершено!")
        break

    if action.isdigit():
        task_num = int(action)
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Справу '{removed_task}' видалено!")
        else:
            print("Невірний номер! Спробуйте ще раз.")
    else:
        print("Будь ласка, введіть число або 'q' для виходу.")

# 3 ЗАВДАННЯ

phonebook = {}

while True:
    print("\n1. Додати контакт\n2. Пошук контакту\n3. Видалити контакт\n4. Вийти")
    choice = input("Виберіть опцію: ")

    if choice == "1":
        name = input("Введіть ім'я: ")
        number = input("Введіть номер: ")
        phonebook[name] = number
        print(f"Контакт {name} додано!")

    elif choice == "2":
        name = input("Введіть ім'я для пошуку: ")
        print(phonebook.get(name, "Контакт не знайдено."))

    elif choice == "3":
        name = input("Введіть ім'я для видалення: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Контакт {name} видалено!")
        else:
            print("Контакт не знайдено.")

    elif choice == "4":
        print("Програму завершено!")
        break

    else:
        print("Невірний вибір, спробуйте ще раз.")

dictionary = {
    "hello": "Привіт",
    "world": "Світ",
    "python": "Пітон",
    "book": "Книга",
    "computer": "Комп'ютер"
}

word = input("Введіть англійське слово: ").lower()
print(dictionary.get(word, "Переклад не знайдено."))

# 4 ЗАВДАННЯ
import re

email = input("Введіть email: ")
pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.(com|ua|org|net)$"

if re.match(pattern, email):
    print("Валідний email!")
else:
    print("Невірний формат email!")

import re

phone = input("Введіть номер телефону: ")
pattern = r"^\+380\d{9}$"

if re.match(pattern, phone):
    print("Валідний номер!")
else:
    print("Помилка! Невірний формат.")


# 5 ЗАВДАННЯ
def convert_currency(amount, currency):
    rates = {"USD": 39.5, "EUR": 42.3, "PLN": 9.2}
    return round(amount / rates.get(currency, 1), 2)


amount = float(input("Введіть суму в грн: "))
currency = input("Виберіть валюту (USD, EUR, PLN): ").upper()

if currency in ["USD", "EUR", "PLN"]:
    print(f"{amount} грн = {convert_currency(amount, currency)} {currency}")
else:
    print("Невідома валюта.")


def square_area(side):
    return side ** 2


side = float(input("Введіть довжину сторони квадрата: "))
print(f"Площа квадрата: {square_area(side)}")

# 6 ЗАВДАННЯ

from datetime import datetime

today = datetime.today()
new_year = datetime(today.year + 1, 1, 1)
days_left = (new_year - today).days

print(f"До Нового року залишилося {days_left} днів!")

from datetime import datetime

birth_date = input("Введіть дату народження (у форматі РРРР-ММ-ДД): ")
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

today = datetime.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

print(f"Вам {age} років.")

# 7 ЗАВДАННЯ

import tkinter as tk


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result_label.config(text=f"Результат: {num1 + num2}")
        elif operation == "-":
            result_label.config(text=f"Результат: {num1 - num2}")
        elif operation == "*":
            result_label.config(text=f"Результат: {num1 * num2}")
        elif operation == "/":
            if num2 != 0:
                result_label.config(text=f"Результат: {num1 / num2}")
            else:
                result_label.config(text="Помилка: ділення на 0!")
    except ValueError:
        result_label.config(text="Помилка: введіть числа!")


root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="+", command=lambda: calculate("+")).pack()
tk.Button(root, text="-", command=lambda: calculate("-")).pack()
tk.Button(root, text="*", command=lambda: calculate("*")).pack()
tk.Button(root, text="/", command=lambda: calculate("/")).pack()

result_label = tk.Label(root, text="Результат:")
result_label.pack()

root.mainloop()


# 8 ЗАВДАННЯ

class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year} р., {self.mileage} км"


class Owner:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        if not self.cars:
            print(f"{self.name} не має машин.")
        else:
            print(f"Машини {self.name}:")
            for car in self.cars:
                print(car)


owner = Owner("Іван")
car1 = Car("Toyota", "Camry", 2020, 45000)
car2 = Car("BMW", "X5", 2018, 85000)

owner.add_car(car1)
owner.add_car(car2)

owner.show_cars()


# 9 ЗАВДАННЯ

class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)

    def show_students(self):
        print(f"Студенти вчителя {self.name}: {', '.join(self.students) if self.students else 'Немає студентів'}")

    def info(self):
        return f"{self.name} - {self.subject}, стаж {self.experience} років."


teacher = Teacher("Ольга", "Математика", 10)
teacher.add_student("Андрій")
teacher.add_student("Марія")
teacher.show_students()
print(teacher.info())
