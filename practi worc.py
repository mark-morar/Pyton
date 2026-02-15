import re
import tkinter as tk


def calculate_balance(wallet, lunch, transport):
    return wallet - (lunch + transport)


def check_balance(balance):
    if balance < 100:
        return "Грошей мало, час економити!"
    else:
        return "Все добре, можна трохи витратити на себе."


expenses_dict = {}

def add_expenses(day, food, transport, other):
    total = food + transport + other
    expenses_dict[f"День {day}"] = total
    return total


def calculate_total_expenses(expenses_dict):
    return sum(expenses_dict.values())

def average_daily_expense(expenses_dict):
    if len(expenses_dict) == 0:
        return 0
    return calculate_total_expenses(expenses_dict) / len(expenses_dict)


root = tk.Tk()
root.title("Облік витрат")
root.geometry("400x300+650+250")

day_counter = 1

def validate_input(value):
    pattern = r"^\d+(\.\d+)?$"
    return re.match(pattern, value)

def add_day():
    global day_counter
    food = food_var.get()
    transport = transport_var.get()
    other = other_var.get()

    if not (validate_input(food) and validate_input(transport) and validate_input(other)):
        result_label.config(text="Помилка: введіть коректні числові значення!", fg="red")
        return

    total = add_expenses(
        day_counter,
        float(food),
        float(transport),
        float(other)
    )
    result_label.config(text=f"День {day_counter}: загальні витрати {total} грн", fg="black")
    day_counter += 1

    food_var.set("")
    transport_var.set("")
    other_var.set("")

def show_results():
    total_expenses = calculate_total_expenses(expenses_dict)
    avg_expense = average_daily_expense(expenses_dict)

    results = "\n".join([f"{day}: {expenses} грн" for day, expenses in expenses_dict.items()])
    results += f"\n\nЗагальні витрати: {total_expenses} грн"
    results += f"\nСередні витрати за день: {avg_expense:.2f} грн"

    result_label.config(text=results, fg="black")


tk.Label(root, text="Витрати на їжу:").pack()
food_var = tk.StringVar()
tk.Entry(root, textvariable=food_var).pack()

tk.Label(root, text="Витрати на транспорт:").pack()
transport_var = tk.StringVar()
tk.Entry(root, textvariable=transport_var).pack()

tk.Label(root, text="Інші витрати:").pack()
other_var = tk.StringVar()
tk.Entry(root, textvariable=other_var).pack()


result_label = tk.Label(root, text="")
result_label.pack()


tk.Button(root, text="Додати день", command=add_day).pack()
tk.Button(root, text="Результати", command=show_results).pack()

root.mainloop()





#part1

wallet = float(input("скільки грошей у гаманці:"))
lunch = float(input("скільки грошей було витрачино на обід:"))
transport = float(input("скільки грошей потрачу на транспорт:"))

ramain_money = wallet - lunch - transport
print(f"у вас залишилось {ramain_money:.2f} грн у гаманці")

if ramain_money < 100:
    print("Грошей мало, час економити!")

else:
    print("Все добре, можна трохи витратити на себе.")

#part 2
num_days = int(input("Скільки днів ви хочете вести облік витрат? "))

total_expenses = 0
expenses_list = []

for day in range(1, num_days + 1):
    print(f"\nДень {day}:")
    food = float(input("Витрати на їжу: "))
    transport = float(input("Витрати на транспорт: "))
    other = float(input("Витрати на інші потреби: "))

    daily_expenses = food + transport + other
    expenses_list.append(daily_expenses)
    total_expenses += daily_expenses

print(f"\nЗагальні витрати за {num_days} днів: {total_expenses:.2f} грн.")

print("Витрати на кожен день:")
for i, daily_expense in enumerate(expenses_list, start=1):
    print(f"День {i}: {daily_expense:.2f} грн")

expenses_dict = {f"День {i+1}": expenses_list[i] for i in range(len(expenses_list))}

print("\nВитрати по днях у словнику:")
for day, expense in expenses_dict.items():
    print(f"{day}: {expense:.2f} грн")


#part3

def calculate_total_expenses(expenses_dict):
    return sum(expenses_dict.values())


def  average_daily_expense(expenses_dict):
    if len(expenses_dict) == 0:
        return 0
    else:
        return calculate_total_expenses(expenses_dict) / len(expenses_dict)


