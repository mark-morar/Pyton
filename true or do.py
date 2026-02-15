# Завдання 1

def check_age():
    try:
        age = int(input("Введіть свій вік: "))
        if age < 0:
            print("Вік не може бути від'ємним. Спробуйте ще раз.")
        elif age > 120:
            print("Вказано занадто великий вік. Перевірте введені дані.")
        else:
            print("Ваш вік коректний:", age)
    except ValueError:
        print("Некоректне введення! Введіть, будь ласка, ціле число.")


check_age()


# Завдання 2

def convert_to_dollars(uah_amount, conversion_rate):
    dollars = uah_amount / conversion_rate
    return dollars

try:
    uah_amount = float(input("Введіть суму у гривнях: "))
    conversion_rate = float(input("Введіть курс конвертації (грн за 1 долар): "))

    if conversion_rate <= 0:
        print("Курс конвертації має бути більше нуля.")
    else:
        dollars = convert_to_dollars(uah_amount, conversion_rate)
        print(f"Сума у доларах: {dollars}")

except ValueError:
    print("Будь ласка, введіть числові значення.")


# Завдання 3

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


try:
    celsius = float(input("Введіть температуру у градусах Цельсія: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Температура у Фаренгейтах: {fahrenheit}")
except ValueError:
    print("Будь ласка, введіть коректне числове значення.")

# Завдання 4
import random
def guess_number_game():
    print("Вітаю в грі 'Вгадай число'! Я загадав число від 1 до 100. Спробуй вгадати!")

    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:

            user_input = input("Введіть число від 1 до 100: ")
            guess = int(user_input)

            if guess < 1 or guess > 100:
                print("Число повинно бути в діапазоні від 1 до 100. Спробуйте ще раз.")
                continue

            attempts += 1

            if guess < target_number:
                print("Загадане число більше. Спробуйте ще раз!")
            elif guess > target_number:
                print("Загадане число менше. Спробуйте ще раз!")
            else:
                print(f"Вітаю! Ви вгадали число {target_number} за {attempts} спроб!")
                break

        except ValueError:
            print("Будь ласка, вводьте тільки цілі числа!")
    guess_number_game()


# Завдання 5

try:
    day = int(input("Введіть день від (1-31): "))
    mounth = int(input("Введіть місяць від (1-12): "))
    year = int(input("Введіть рік: "))

    if mounth < 1 or mounth > 12:
        raise ValueError ("місяць має бути в діапазоні від 1 до 12 ")

    if mounth == 2 and day > 29:
        raise ValueError("у лютому може бути максимум  29 днів")

    if day < 1 or day > 31:
        raise ValueError("дні у місяці мают бути в діапазоні від 1 до 31")

except ValueError as e:
    print(f"помилка {e}")

else:
    print(f"дата:{day} - {mounth} - {year}")























