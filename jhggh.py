score = 0
def my_score():

    global score

    score+=5

    print(f"Ваш рахунок - {score}")


my_score()
my_score()
my_score()


def my_local_score():

    score = 0


    score  += 5

    print(f"Ваш рахунок - {score}")

my_local_score()
my_local_score()
my_local_score()


#Завдання 1

total = 0

def add_to_cart(price):

    global total
    if price > 0:
        total += price
        print(f"Товар додано до кошика. Поточна сума: {total} грн.")
    else:
        print("Ціна повинна бути додатним числом!")


add_to_cart(150.5)
add_to_cart(249.99)
add_to_cart(99.99)

print(f"Загальна сума покупок: {total} грн.")

# Завдання 2

glasses_drunk = 0

def drink_water():

    global glasses_drunk
    glasses_drunk += 1
    print(f"Ви випили {glasses_drunk} склянку води.")

    if glasses_drunk == 8:
        print("Ви досягли денного мінімуму!")

    elif glasses_drunk > 8:
        print("Чудово! Ви перевищили мінімум для гарного самопочуття.")

drink_water()
drink_water()
drink_water()
drink_water()
drink_water()
drink_water()
drink_water()
drink_water()
drink_water()


# Завдання 3

steps_count = 0

def add_steps(count):
    global steps_count
    if count < 0:
        print("Кількість кроків не може бути від'ємною!")


    steps_count += count
    print(f"Додано {count} кроків. Загальна кількість: {steps_count}")


    if steps_count >= 10000:
        print("Ви досягли своєї мети на сьогодні!")

add_steps(5000)
add_steps(3000)
add_steps(2000)
add_steps(-100)


# Завдання 4

budget = 1000

def spend_money(amount):
    global budget
    if amount < 0:
        print("Сума витрат не може бути від'ємною!")
        return

    budget -= amount
    print(f"Ви витратили {amount} грн. Залишок бюджету: {budget} грн.")

    if budget < 0:
        print("Увага! Ви перевищили бюджет!")

spend_money(200)
spend_money(500)
spend_money(400)
spend_money(-50)




































































