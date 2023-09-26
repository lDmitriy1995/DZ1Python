import re

# Дескриптор для имени
class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name
    
    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError("Имя должно состоять только из букв")
        instance._name = value

# Дескриптор для возраста
class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance._age
    
    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Возраст должен быть положительным целым числом")
        instance._age = value

# Дескриптор для email
class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email
    
    def __set__(self, instance, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Неверный формат email")
        instance._email = value

# Класс User с использованием дескрипторов
class User:
    name = NameDescriptor()
    age = AgeDescriptor()
    email = EmailDescriptor()
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Пример использования
if __name__ == "__main__":
    # Создаем пользователей с использованием класса User
    user1 = User("Alice", 25, "alice@example.com")
    user2 = User("Bob", 30, "bob@example.com")

    # Попытка создать пользователя с некорректными данными вызовет ошибку
    try:
        invalid_user = User("123", -5, "invalid-email")
    except ValueError as e:
        print(e)

    # Пример создания базы данных
    class Database:
        def __init__(self):
            self.users = []
        
        def add_user(self, user):
            self.users.append(user)
        
        def remove_user(self, user):
            self.users.remove(user)
        
        def find_users_by_name(self, name):
            return [user for user in self.users if user.name == name]
        
        def find_users_by_age(self, age):
            return [user for user in self.users if user.age == age]
        
        def find_users_by_email(self, email):
            return [user for user in self.users if user.email == email]

    # Создаем базу данных и добавляем пользователей
    db = Database()
    db.add_user(user1)
    db.add_user(user2)

    # Поиск пользователей по различным критериям
    print("Пользователи с именем Alice:")
    for user in db.find_users_by_name("Alice"):
        print(user.name)

    print("Пользователи возрастом 30 лет:")
    for user in db.find_users_by_age(30):
        print(user.name)

    print("Пользователи с email bob@example.com:")
    for user in db.find_users_by_email("bob@example.com"):
        print(user.name)
