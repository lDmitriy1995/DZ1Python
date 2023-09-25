import pickle

class Employee:
    def __init__(self, first_name, last_name, age, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, Department: {self.department}"

class EmployeeDatabase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.employees = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, 'rb') as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = []

    def save_data(self):
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.employees, file)

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_data()

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            self.save_data()

    def search_by_last_name(self, last_name):
        result = [employee for employee in self.employees if employee.last_name == last_name]
        return result

    def filter_by_age(self, age):
        result = [employee for employee in self.employees if employee.age == age]
        return result

    def filter_by_last_name_starting_with(self, letter):
        result = [employee for employee in self.employees if employee.last_name.startswith(letter)]
        return result

    def list_all_employees(self):
        for employee in self.employees:
            print(employee)

# Пример использования:
if __name__ == "__main__":
    database = EmployeeDatabase("employees.pkl")
    
    while True:
        print("\nСотрудники: ")
        database.list_all_employees()

        print("\nМеню:")
        print("1. Добавить сотрудника")
        print("2. Удалить сотрудника")
        print("3. Поиск по фамилии")
        print("4. Фильтр по возрасту")
        print("5. Фильтр по фамилии (по первой букве)")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            first_name = input("Введите имя сотрудника: ")
            last_name = input("Введите фамилию сотрудника: ")
            age = int(input("Введите возраст сотрудника: "))
            department = input("Введите отдел сотрудника: ")
            employee = Employee(first_name, last_name, age, department)
            database.add_employee(employee)
        elif choice == "2":
            last_name = input("Введите фамилию сотрудника для удаления: ")
            employees_to_remove = database.search_by_last_name(last_name)
            if employees_to_remove:
                print("Сотрудники для удаления:")
                for i, employee in enumerate(employees_to_remove, 1):
                    print(f"{i}. {employee}")
                index_to_remove = int(input("Выберите номер сотрудника для удаления: ")) - 1
                if 0 <= index_to_remove < len(employees_to_remove):
                    database.remove_employee(employees_to_remove[index_to_remove])
            else:
                print("Сотрудник с такой фамилией не найден.")
        elif choice == "3":
            last_name = input("Введите фамилию для поиска: ")
            found_employees = database.search_by_last_name(last_name)
            if found_employees:
                print("Найденные сотрудники:")
                for employee in found_employees:
                    print(employee)
            else:
                print("Сотрудники с такой фамилией не найдены.")
        elif choice == "4":
            age = int(input("Введите возраст для фильтрации: "))
            filtered_employees = database.filter_by_age(age)
            if filtered_employees:
                print("Сотрудники с указанным возрастом:")
                for employee in filtered_employees:
                    print(employee)
            else:
                print("Сотрудники с указанным возрастом не найдены.")
        elif choice == "5":
            letter = input("Введите первую букву фамилии для фильтрации: ")
            filtered_employees =
