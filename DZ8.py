# Задание 1
def product_of_elements(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Задание 2
def find_minimum(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

# Задание 3
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes_in_list(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count

# Задание 4
def remove_from_list(numbers, to_remove):
    count = 0
    for num in to_remove:
        while num in numbers:
            numbers.remove(num)
            count += 1
    return count

# Задание 5
def merge_lists(list1, list2):
    return list1 + list2

# Задание 6
def power_of_elements(numbers, power):
    result = [num ** power for num in numbers]
    return result

# Примеры использования функций
numbers_list = [2, 3, 5, 7, 10]

# Задание 1
product = product_of_elements(numbers_list)
print("Произведение элементов:", product)

# Задание 2
minimum = find_minimum(numbers_list)
print("Минимальный элемент:", minimum)

# Задание 3
prime_count = count_primes_in_list(numbers_list)
print("Количество простых чисел:", prime_count)

# Задание 4
to_remove = [5, 10]
removed_count = remove_from_list(numbers_list, to_remove)
print("Удалено элементов:", removed_count)
print("Список после удаления:", numbers_list)

# Задание 5
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print("Объединенный список:", merged_list)

# Задание 6
power_result = power_of_elements(numbers_list, 2)
print("Степени элементов:", power_result)
