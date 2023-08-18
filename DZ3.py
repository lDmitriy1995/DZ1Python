
#Задание 1

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

choice = input("Выберите операцию (сумма/произведение): ")

if choice == "сумма":
    result = num1 + num2 + num3
    print("Сумма чисел:", result)
elif choice == "произведение":
    result = num1 * num2 * num3
    print("Произведение чисел:", result)
else:
    print("Неверный выбор операции")


#Задание 2

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

choice = input("Выберите операцию (максимум/минимум/среднее): ")

if choice == "максимум":
    result = max(num1, num2, num3)
    print("Максимум:", result)
elif choice == "минимум":
    result = min(num1, num2, num3)
    print("Минимум:", result)
elif choice == "среднее":
    result = (num1 + num2 + num3) / 3
    print("Среднее арифметическое:", result)
else:
    print("Неверный выбор операции")


#Задание 3

meters = float(input("Введите количество метров: "))
choice = input("Выберите единицу измерения (мили/дюймы/ярды): ")

if choice == "мили":
    result = meters * 0.000621371
    print("Метры в милях:", result)
elif choice == "дюймы":
    result = meters * 39.3701
    print("Метры в дюймах:", result)
elif choice == "ярды":
    result = meters * 1.09361
    print("Метры в ярдах:", result)
else:
    print("Неверный выбор единицы измерения")
