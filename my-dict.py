contacts = {}
def show_contacts():
    if not contacts:
        print("Телефонна книга порожня.")
    else:
        print("Контакти:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
def add_contact():
    name = input("Введіть ім'я: ")
    phone = input("Введіть номер телефону: ")
    if name in contacts:
        print(f"Контакт {name} вже існує.")
    else:
        contacts[name] = phone
        print(f"Контакт {name} успішно додано.")
def search_contact():
    name = input("Введіть ім'я для пошуку: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Контакт {name} не знайдено.")
def main_menu():
    while True:
        print("\n#Меню")
        print("1. Показати всі контакти")
        print("2. Додати новий контакт")
        print("3. Знайти контакт")
        print("4. Вихід")
        choice = input("Оберіть дію (1-4): ")
        if choice == '1':
            show_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
main_menu()


import tkinter as tk

root = tk.Tk()

root.title("First Window")

root.geometry("600x400+700+300")

label_1 = tk.Label(text = "Hello ItStep",
                   font = ("Arial",40,"bold"),
                   fg = "blue",
                   bg = "yellow",
                   height = 3,
                   padx=30,
                   pady=30)

label_1.pack()

root.mainloop()


# Завдання 1

menu = {}

while True:
    print("\n--- Меню ---")
    print("1. Додати страву")
    print("2. Показати меню")
    print("3. Підрахувати загальну суму замовлення")
    print("4. Вийти")

    choice = input("Оберіть опцію (1-4): ")
    if choice == "1":

        dish = input("Введіть назву страви: ")
        if dish in menu:
            print("Ця страва вже є у меню. Її ціна оновиться.")
        try:
            price = float(input("Введіть ціну страви: "))
            menu[dish] = price
            print(f"Страву '{dish}' додано до меню із ціною {price:.2f}.")
        except ValueError:
            print("Ціна повинна бути числом. Спробуйте ще раз.")

    elif choice == "2":

        if not menu:
            print("Меню порожнє.")
        else:
            print("\nПоточне меню:")
            for dish, price in menu.items():
                print(f"- {dish}: {price:.2f} грн")

    elif choice == "3":

        if not menu:
            print("Меню порожнє. Додайте страви, щоб підрахувати суму.")
        else:
            total_sum = sum(menu.values())
            print(f"Загальна сума замовлення: {total_sum:.2f} грн")

    elif choice == "4":
        print("Вихід із програми. Гарного дня!")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")



#Завдання 2
import tkinter as tk

root = tk.Tk()
root.title("Гра: Вгадай число")
root.geometry("400x300+650+250")

label_title = tk.Label(root, text="Вгадай число від 1 до 100", font=("Arial", 14))
label_title.pack(pady=10)

entry_guess = tk.Entry(root, font=("Arial", 12))
entry_guess.pack(pady=10)

btn_submit = tk.Button(root, text="Спробувати", font=("Arial", 12))
btn_submit.pack(pady=10)

label_feedback = tk.Label(root, text="Введіть число та натисніть 'Спробувати'", font=("Arial", 12))
label_feedback.pack(pady=20)

root.mainloop()




















