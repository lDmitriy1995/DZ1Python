#Задание 1
def count_word_occurrences(file_name, word_to_count):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            occurrences = content.lower().count(word_to_count.lower())
            return occurrences
    except FileNotFoundError:
        return 0

# Пример использования:
file_name = 'your_file.txt'  # Укажите имя вашего текстового файла
word_to_count = 'example'   # Замените 'example' на слово, которое вы хотите посчитать
count = count_word_occurrences(file_name, word_to_count)
print(f'Слово "{word_to_count}" встречается {count} раз в файле {file_name}.')


#Задание 2

def replace_word_in_file(file_name, word_to_replace, replacement_word):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        
        updated_content = content.replace(word_to_replace, replacement_word)
        
        with open(file_name, 'w') as file:
            file.write(updated_content)
            
    except FileNotFoundError:
        print(f'Файл {file_name} не найден.')

# Пример использования:
file_name = 'your_file.txt'       # Укажите имя вашего текстового файла
word_to_replace = 'old_word'      # Замените 'old_word' на слово, которое вы хотите заменить
replacement_word = 'new_word'    # Замените 'new_word' на новое слово
replace_word_in_file(file_name, word_to_replace, replacement_word)
