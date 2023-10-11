#Задание 1 

# Создаем пустой список для чисел
numbers = []

while True:
    print("Меню:")
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка (с начала или с конца)")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке (первое или все вхождения)")
    print("6. Выход")

    choice = input("Выберите действие (1/2/3/4/5/6): ")

    if choice == "1":
        new_number = int(input("Введите число: "))
        if new_number in numbers:
            print("Это число уже есть в списке.")
        else:
            numbers.append(new_number)
    elif choice == "2":
        number_to_remove = int(input("Введите число для удаления: "))
        if number_to_remove in numbers:
            numbers.remove(number_to_remove)
        else:
            print("Это число не найдено в списке.")
    elif choice == "3":
        direction = input("Показать содержимое списка (начало/конец): ")
        if direction == "начало":
            print(numbers)
        else:
            print(numbers[::-1])
    elif choice == "4":
        check_number = int(input("Введите число для проверки: "))
        if check_number in numbers:
            print(f"Число {check_number} найдено в списке.")
        else:
            print(f"Число {check_number} не найдено в списке.")
    elif choice == "5":
        replace_number = int(input("Введите число для замены: "))
        if replace_number in numbers:
            replacement = int(input("Введите новое значение: "))
            all_occurrences = input("Заменить все вхождения (да/нет): ")
            if all_occurrences == "да":
                while replace_number in numbers:
                    index = numbers.index(replace_number)
                    numbers[index] = replacement
            else:
                index = numbers.index(replace_number)
                numbers[index] = replacement
        else:
            print(f"Число {replace_number} не найдено в списке.")
    elif choice == "6":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

print("Программа завершена.")

#Задание 2

class StringStack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        if len(self.stack) < self.max_size:
            self.stack.append(string)
            print(f"Строка '{string}' добавлена в стек.")
        else:
            print("Стек полон, нельзя добавить новую строку.")

    def pop(self):
        if self.stack:
            popped_string = self.stack.pop()
            print(f"Извлечена строка '{popped_string}' из стека.")
        else:
            print("Стек пуст, нельзя извлечь строку.")

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def clear(self):
        self.stack.clear()
        print("Стек очищен.")

    def get_top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None


stack = StringStack(5)  # Создаем стек с максимальным размером 5

stack.push("Строка 1")
stack.push("Строка 2")
stack.push("Строка 3")
stack.push("Строка 4")
stack.push("Строка 5")

stack.push("Строка 6")  # Превышение размера стека, выведет сообщение об этом

stack.pop()  # Извлекаем строку

print(f"Количество строк в стеке: {stack.count()}")
print(f"Стек пустой? {stack.is_empty()}")
print(f"Стек полный? {stack.is_full()}")

stack.clear()  # Очищаем стек

top_string = stack.get_top()
if top_string:
    print(f"Верхняя строка в стеке: {top_string}")
else:
    print("Стек пуст.")



