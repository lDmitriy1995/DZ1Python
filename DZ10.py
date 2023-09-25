
#Задание 1
# Создаем списки с идентификационными кодами и телефонными номерами
codes = [101, 102, 103, 104, 105]
phones = ['555-101', '555-102', '555-103', '555-104', '555-105']

def display_menu():
    print("Меню:")
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефона")
    print("3. Вывести список пользователей с кодами и телефонами")
    print("4. Выход")

def sort_by_codes():
    sorted_data = sorted(zip(codes, phones), key=lambda x: x[0])
    return sorted_data

def sort_by_phones():
    sorted_data = sorted(zip(codes, phones), key=lambda x: x[1])
    return sorted_data

while True:
    display_menu()
    choice = input("Выберите действие (1/2/3/4): ")
    
    if choice == '1':
        sorted_data = sort_by_codes()
        for code, phone in sorted_data:
            print(f"Код: {code}, Телефон: {phone}")
    elif choice == '2':
        sorted_data = sort_by_phones()
        for code, phone in sorted_data:
            print(f"Код: {code}, Телефон: {phone}")
    elif choice == '3':
        for i in range(len(codes)):
            print(f"Код: {codes[i]}, Телефон: {phones[i]}")
    elif choice == '4':
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз.")






#Задание 2

# Создаем списки с названиями книг и годами выпуска
books = ['Книга 1', 'Книга 2', 'Книга 3', 'Книга 4', 'Книга 5']
years = [2000, 1995, 2010, 1987, 2005]

def display_menu():
    print("Меню:")
    print("1. Отсортировать по названию книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг с названиями и годами выпуска")
    print("4. Выход")

def sort_by_titles():
    sorted_data = sorted(zip(books, years), key=lambda x: x[0])
    return sorted_data

def sort_by_years():
    sorted_data = sorted(zip(books, years), key=lambda x: x[1])
    return sorted_data

while True:
    display_menu()
    choice = input("Выберите действие (1/2/3/4): ")
    
    if choice == '1':
        sorted_data = sort_by_titles()
        for book, year in sorted_data:
            print(f"Название: {book}, Год выпуска: {year}")
    elif choice == '2':
        sorted_data = sort_by_years()
        for book, year in sorted_data:
            print(f"Название: {book}, Год выпуска: {year}")
    elif choice == '3':
        for i in range(len(books)):
            print(f"Название: {books[i]}, Год выпуска: {years[i]}")
    elif choice == '4':
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз.")

