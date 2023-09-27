#Задание 1

# Открываем файлы для чтения
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

# Проверяем совпадение строк
for line1, line2 in zip(lines1, lines2):
    if line1 != line2:
        print(f"Файл 1: {line1}")
        print(f"Файл 2: {line2}")

# Если файлы имеют разное количество строк
if len(lines1) > len(lines2):
    print(f"Файл 1: {lines1[len(lines2)]}")
elif len(lines1) < len(lines2):
    print(f"Файл 2: {lines2[len(lines1)]}")



#Задание 2

# Открываем файл для чтения
with open('input.txt', 'r') as input_file:
    content = input_file.read()

# Инициализируем счетчики
char_count = len(content)
line_count = content.count('\n')
vowels_count = sum(1 for char in content if char.lower() in 'aeiouаоиеёэыуюя')
consonants_count = char_count - vowels_count
digits_count = sum(1 for char in content if char.isdigit())

# Записываем статистику в новый файл
with open('stats.txt', 'w') as stats_file:
    stats_file.write(f"Количество символов: {char_count}\n")
    stats_file.write(f"Количество строк: {line_count}\n")
    stats_file.write(f"Количество гласных букв: {vowels_count}\n")
    stats_file.write(f"Количество согласных букв: {consonants_count}\n")
    stats_file.write(f"Количество цифр: {digits_count}\n")



#Задание 3

# Открываем файл для чтения
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

# Удаляем последнюю строку
lines.pop()

# Записываем результат в новый файл
with open('output.txt', 'w') as output_file:
    output_file.writelines(lines)


#Задание 4

# Открываем файл для чтения
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

# Находим длину самой длинной строки
max_length = max(len(line) for line in lines)

print(f"Длина самой длинной строки: {max_length} символов")



#Задание 5


# Запрос от пользователя
word_to_count = input("Введите слово для поиска: ")

# Открываем файл для чтения
with open('input.txt', 'r') as input_file:
    content = input_file.read()

# Считаем количество вхождений слова
count = content.lower().count(word_to_count.lower())

print(f"Слово '{word_to_count}' встречается {count} раз.")



#Задание 6


# Запрос от пользователя
word_to_find = input("Введите слово для поиска: ")
word_to_replace = input("Введите слово для замены: ")

# Открываем файл для чтения
with open('input.txt', 'r') as input_file:
    content = input_file.read()

# Заменяем слово
new_content = content.replace(word_to_find, word_to_replace)

# Записываем результат в новый файл
with open('output.txt', 'w') as output_file:
    output_file.write(new_content)



