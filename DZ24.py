numbers = []

while True:
    print("Меню:")
    print("1. Добавить число в список")
    print("2. Удалить число из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить наличие числа в списке")
    print("5. Заменить число в списке")
    print("0. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        num = int(input("Введите число для добавления: "))
        if num not in numbers:
            numbers.append(num)
            print("Число добавлено в список.")
        else:
            print("Число уже существует в списке.")

    elif choice == "2":
        num = int(input("Введите число для удаления: "))
        if num in numbers:
            numbers.remove(num)
            print("Число удалено из списка.")
        else:
            print("Число не найдено в списке.")

    elif choice == "3":
        reverse = input("Показать список с начала (1) или с конца (2): ")
        if reverse == "1":
            print(numbers)
        elif reverse == "2":
            print(numbers[::-1])

    elif choice == "4":
        num = int(input("Введите число для проверки: "))
        if num in numbers:
            print("Число найдено в списке.")
        else:
            print("Число не найдено в списке.")

    elif choice == "5":
        num = int(input("Введите число для замены: "))
        new_num = int(input("Введите новое число: "))
        if num in numbers:
            index = numbers.index(num)
            numbers[index] = new_num
            print("Число заменено в списке.")
        else:
            print("Число не найдено в списке.")

    elif choice == "0":
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз.")

class StringStack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

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


Чтобы выполнить третье задание, вам нужно просто удалить параметр max_size
