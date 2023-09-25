def calculate_powers(numbers, power):
    result = [num ** power for num in numbers]
    return result

# Пример использования:
numbers = [1, 2, 3, 4, 5]
power = 2
result = calculate_powers(numbers, power)
print(result)
