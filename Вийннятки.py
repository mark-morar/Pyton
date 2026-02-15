#Завдання 1

try:

    name = input("Введіть ваше ім'я: ")
    age = int(input("\nВведіть ваш вік: "))

    if age < 0 or age > 130:
        raise ValueError("Вік повинен бути в діапазоні від 0 до 130.")

    print(f"\nПривіт, {name}! Твій вік — {age}.")
except ValueError as e:

    print(f"Помилка: {e}")

# Завдання 2

def format_greeting(name, age):

    if age < 0 or age > 130:
        raise ValueError("Вік повинен бути в діапазоні від 0 до 130.")
    return f"Привіт, {name}! Твій вік — {age}."

try:
    user_name = input("Введіть ваше ім'я: ")
    user_age = int(input("Введіть ваш вік: "))
    print(format_greeting(user_name, user_age))
except ValueError as e:
    print(f"Помилка: {e}")


# Завдання 3

numbers = []
print("Введіть додатні числа. Для завершення введіть 'стоп'.")

while True:
    user_input = input("Введіть число: ")

    if user_input.lower() == 'стоп':
        break

    try:
        number = float(user_input)
        if number < 0:
            raise ValueError("Знайдено від'ємне число!")
        numbers.append(number)
    except ValueError as e:
        print(f"Помилка: {e}")
        exit()

if not numbers:
    print("Список чисел порожній.")
else:
    print(f"Сума всіх додатніх чисел: {sum(numbers)}")

# Завдання 4

def main():
    try:
        numbers = []
        print("Введіть додатні числа. Для завершення введіть 'стоп'.")

        while True:
            user_input = input("Введіть число: ")

            if user_input.lower() == 'стоп':
                break

            try:
                number = float(user_input)
                if number < 0:
                    raise ValueError("Знайдено від'ємне число!")
                numbers.append(number)
            except ValueError as e:
                print(f"Помилка: {e}")
                return

        if not numbers:
            print("Список чисел порожній.")
        else:
            print(f"Сума всіх додатніх чисел: {sum(numbers)}")

    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")

if __name__ == "__main__":
    main()










































































