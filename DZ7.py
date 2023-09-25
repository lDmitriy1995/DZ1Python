# Задание 1
def display_quote():
    quote = "Don't let the noise of others' opinions\n" \
            "drown out your own inner voice."
    author = "Steve Jobs"
    print(quote)
    print(author)

# Задание 2
def display_odd_numbers(num1, num2):
    for num in range(num1, num2 + 1):
        if num % 2 != 0:
            print(num)

# Задание 3
def display_line(length, direction, symbol):
    if direction == "горизонталь":
        print(symbol * length)
    elif direction == "вертикаль":
        for _ in range(length):
            print(symbol)

# Задание 4
def max_of_four(num1, num2, num3, num4):
    return max(num1, num2, num3, num4)

# Задание 5
def sum_in_range(start, end):
    return sum(range(start, end + 1))

# Задание 6
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

# Задание 7
def is_happy_six_digit_number(number):
    if len(str(number)) != 6:
        return False
    first_half = str(number)[:3]
    second_half = str(number)[3:]
    return sum(map(int, first_half)) == sum(map(int, second_half))

# Теперь можно вызывать эти функции при необходимости


# Задание 1
display_quote()

# Задание 2
display_odd_numbers(1, 10)

# Задание 3
display_line(5, "горизонталь", "*")
display_line(3, "вертикаль", "|")

# Задание 4
result = max_of_four(12, 7, 9, 14)
print(result)

# Задание 5
total_sum = sum_in_range(1, 10)
print(total_sum)

# Задание 6
is_prime_result = is_prime(17)
print(is_prime_result)

# Задание 7
is_happy = is_happy_six_digit_number(123420)
print(is_happy)





