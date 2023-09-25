#Задание 1

from sympy import sympify

# Запрос арифметического выражения от пользователя
expression = input("Введите арифметическое выражение (например, 23+12): ")

try:
    # Преобразуем строку в объект выражения
    expr = sympify(expression)
    
    # Вычисляем результат выражения
    result = expr.evalf()
    
    print(f"Результат: {result}")
except Exception as e:
    print("Ошибка: некорректное выражение или деление на ноль.")




#Задание 2


import random

# Создаем случайный список целых чисел
random_numbers = [random.randint(-10, 10) for _ in range(20)]

# Инициализируем переменные для минимального и максимального элементов
min_number = float('inf')
max_number = float('-inf')

# Инициализируем переменные для подсчета отрицательных, положительных и нулевых элементов
negative_count = 0
positive_count = 0
zero_count = 0

# Перебираем элементы списка
for number in random_numbers:
    # Находим минимальный элемент
    if number < min_number:
        min_number = number

    # Находим максимальный элемент
    if number > max_number:
        max_number = number

    # Подсчитываем отрицательные, положительные и нулевые элементы
    if number < 0:
        negative_count += 1
    elif number > 0:
        positive_count += 1
    else:
        zero_count += 1

# Выводим результаты на экран
print("Список случайных чисел:", random_numbers)
print("Минимальный элемент:", min_number)
print("Максимальный элемент:", max_number)
print("Количество отрицательных элементов:", negative_count)
print("Количество положительных элементов:", positive_count)
print("Количество нулей:", zero_count)
