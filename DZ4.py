#Задание 1

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

print(f"Простые числа в диапазоне от {start} до {end}:")

for num in range(start, end + 1):
    if is_prime(num):
        print(num)

#Задание 2

for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}", end="\t")
    print()


#Задание 3

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for i in range(start, end + 1):
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}", end="\t")
    print()
