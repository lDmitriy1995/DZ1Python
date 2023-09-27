#Задание 1

class BasketballPlayerDatabase:
    def __init__(self):
        self.players = {}
    
    def add_player(self, name, height):
        self.players[name] = height
    
    def remove_player(self, name):
        if name in self.players:
            del self.players[name]
        else:
            print(f"{name} не найден в базе данных.")
    
    def find_player(self, name):
        if name in self.players:
            return f"{name}: Рост - {self.players[name]} см"
        else:
            return f"{name} не найден в базе данных."
    
    def update_player(self, name, height):
        if name in self.players:
            self.players[name] = height
        else:
            print(f"{name} не найден в базе данных.")
    
    def show_all_players(self):
        for name, height in self.players.items():
            print(f"{name}: Рост - {height} см")

# Пример использования
if __name__ == "__main__":
    database = BasketballPlayerDatabase()
    
    # Добавляем информацию о баскетболистах
    database.add_player("Michael Jordan", 198)
    database.add_player("LeBron James", 206)
    database.add_player("Kobe Bryant", 198)
    
    # Поиск баскетболиста
    print(database.find_player("Michael Jordan"))
    print(database.find_player("Magic Johnson"))
    
    # Обновление информации о баскетболисте
    database.update_player("LeBron James", 205)
    
    # Удаление баскетболиста
    database.remove_player("Kobe Bryant")
    
    # Вывод всех баскетболистов
    database.show_all_players()




#Задание 2

class EnglishFrenchDictionary:
    def __init__(self):
        self.dictionary = {}
    
    def add_word(self, english_word, french_translation):
        self.dictionary[english_word] = french_translation
    
    def remove_word(self, english_word):
        if english_word in self.dictionary:
            del self.dictionary[english_word]
        else:
            print(f"{english_word} не найден в словаре.")
    
    def find_translation(self, english_word):
        if english_word in self.dictionary:
            return f"{english_word}: {self.dictionary[english_word]}"
        else:
            return f"{english_word} не найден в словаре."
    
    def update_translation(self, english_word, french_translation):
        if english_word in self.dictionary:
            self.dictionary[english_word] = french_translation
        else:
            print(f"{english_word} не найден в словаре.")
    
    def show_all_words(self):
        for english_word, french_translation in self.dictionary.items():
            print(f"{english_word}: {french_translation}")

# Пример использования
if __name__ == "__main__":
    dictionary = EnglishFrenchDictionary()
    
    # Добавляем слова в словарь
    dictionary.add_word("apple", "pomme")
    dictionary.add_word("banana", "banane")
    dictionary.add_word("cat", "chat")
    
    # Поиск перевода слова
    print(dictionary.find_translation("apple"))
    print(dictionary.find_translation("dog"))
    
    # Обновление перевода слова
    dictionary.update_translation("banana", "banane jaune")
    
    # Удаление слова из словаря
    dictionary.remove_word("cat")
    
    # Вывод всех слов
    dictionary.show_all_words()




#Задание 3

class CompanyDatabase:
    def __init__(self):
        self.companies = {}
    
    def add_company(self, name, phone, email, position, office, skype):
        self.companies[name] = {
            "Phone": phone,
            "Email": email,
            "Position": position,
            "Office": office,
            "Skype": skype
        }
    
    def remove_company(self, name):
        if name in self.companies:
            del self.companies[name]
        else:
            print(f"{name} не найден в базе данных.")
    
    def find_company(self, name):
        if name in self.companies:
            return self.companies[name]
        else:
            return f"{name} не найден в базе данных."
    
    def update_company(self, name, field, value):
        if name in self.companies:
            if field in self.companies[name]:
                self.companies[name][field] = value
            else:
                print(f"{field} не существует в информации о компании.")
        else:
            print(f"{name} не найден в базе данных.")
    
    def show_all_companies(self):
        for name, info in self.companies.items():
            print(f"Компания: {name}")
            for field, value in info.items():
                print(f"{field}: {value}")

# Пример использования
if __name__ == "__main__":
    database = CompanyDatabase()
    
    # Добавляем информацию о компаниях
    database.add_company("Company A", "+123456789", "info@companya.com", "Manager", 101, "companya_skype")
    database.add_company("Company B", "+987654321", "info@companyb.com", "Engineer", 202, "companyb_skype")
    database.add_company("Company C", "+111111111", "info@companyc.com", "Designer", 303, "companyc_skype")
    
    # Поиск информации о компании
    print(database.find_company("Company A"))
    print(database.find_company("Company D"))
    
    # Обновление информации о компании
    database.update_company("Company B", "Phone", "+999999999")
    
    # Удаление компании
    database.remove_company("Company C")
    
    # Вывод информации о всех компаниях
    database.show_all_companies()




#Задание 4

class BookCollection:
    def __init__(self):
        self.books = {}
    
    def add_book(self, author, title, genre, year, pages, publisher):
        self.books[title] = {
            "Author": author,
            "Genre": genre,
            "Year": year,
            "Pages": pages,
            "Publisher": publisher
        }
    
    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
        else:
            print(f"{title} не найдена в коллекции.")
    
    def find_book(self, title):
        if title in self.books:
            return self.books[title]
        else:
            return f"{title} не найдена в коллекции."
    
    def update_book(self, title, field, value):
        if title in self.books:
            if field in self.books[title]:
                self.books[title][field] = value
            else:
                print(f"{field} не существует в информации о книге.")
        else:
            print(f"{title} не найдена в коллекции.")
    
    def show_all_books(self):
        for title, info in self.books.items():
            print(f"Книга: {title}")
            for field, value in info.items():
                print(f"{field}: {value}")

# Пример использования
if __name__ == "__main__":
    collection = BookCollection()
    
    # Добавляем информацию о книгах
    collection.add_book("Author A", "Book 1", "Fiction", 2000, 300, "Publisher X")
    collection.add_book("Author B", "Book 2", "Mystery", 1995, 250, "Publisher Y")
    collection.add_book("Author C", "Book 3", "Science Fiction", 2010, 400, "Publisher Z")
    
    # Поиск информации о книге
    print(collection.find_book("Book 1"))
    print(collection.find_book("Book 4"))
    
    # Обновление информации о книге
    collection.update_book("Book 2", "Pages", 280)
    
    # Удаление книги из коллекции
    collection.remove_book("Book 3")
    
    # Вывод информации о всех книгах
    collection.show_all_books()






