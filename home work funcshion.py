# Завдання 1
def display_quote():
    print('"Don\'t compare yourself with anyone in this world…')
    print('if you do so, you are insulting yourself."')

# Виклик функції
display_quote()



# Завдання 2
def display_even_numbers(start, end):

    if start > end:
        start, end = end, start

    print(f"Парні числа між {start} та {end}:")
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end=" ")
    print()


display_even_numbers(3, 15)
display_even_numbers(10, 2)



# Завдання 3

def draw_square(size, char, filled):
    if size < 1:
        print("Розмір квадрата має бути більше 0.")
        return

    for i in range(size):
        if filled or i == 0 or i == size - 1:

            print(char * size)
        else:

            print(char + ' ' * (size - 2) + char)

draw_square(5, '*', True)
print()
draw_square(5, '*', False)



# Завдання 4

def minimal(lis):
    min_number = lis[0]
    for element in lis:
        if element < min_number:
            min_number = element

        return min_number

numbers1 = [10,4,80,77,4]
min1 = minimal(numbers1)

numbers2 = [43,67,98,4,1]
minimal(numbers2)


# Завдання 5

def product_of_range(start, end):
    # Якщо межі переплутані, міняємо їх місцями
    if start > end:
        start, end = end, start

    product = 1
    for number in range(start, end + 1):
        product *= number

    return product



print(product_of_range(5, 25))
print(product_of_range(25, 5))


# Задання 6

def display_even_numbers(start, end):
    # Якщо межі переплутані, міняємо їх місцями
    if start > end:
        start, end = end, start

    print(f"Парні числа між {start} та {end}:")
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end=" ")
    print()



display_even_numbers(3, 15)
display_even_numbers(10, 2)


# Завдання 7

def is_palindrome(number):


    str_number = str(number)

    return str_number == str_number[::-1]

print(is_palindrome(123321))
print(is_palindrome(546645))
print(is_palindrome(421987))

list_num1 = [32,45,679,45,75,787,"#"]
list_num2 = [32,54,67,45,89,0,9,"?"]

print("третій список")
list_num3 = list_num1 + list_num2
print(list_num3)

print("третій список без повторів")
list_num3 =list(set(list_num1 + list_num2))
print(list_num3)

print("третій список з спільними елементами двух списків")
list_num3 = list(set(list_num1) & set(list_num2))
print(list_num3)

print("третій список що містить унікальні елементи двух списків")
list_num3 = list(set(list_num1) ^ set(list_num2))
print(list_num3)


temperatures = [15,18,20,17,19,22,26,12,15,20]
check = ""
day = 0
for temp in range(len(temperatures)):
  print(temperatures[temp])

print("середня температура за тиждень")
print(sum(temperatures)/len(temperatures))







































































