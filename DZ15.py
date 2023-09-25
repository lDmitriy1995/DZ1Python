import pickle

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__(x, y)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return 3.14159 * self.width * self.height

    def perimeter(self):
        # Это приближенное значение периметра эллипса
        h = ((self.width - self.height) ** 2) / ((self.width + self.height) ** 2)
        return 3.14159 * (self.width + self.height) * (1 + (3 * h) / (10 + (4 - 3 * h) ** 0.5))

# Создание и сохранение фигур в файл
shapes = [Square(0, 0, 5), Rectangle(0, 0, 4, 6), Circle(0, 0, 3), Ellipse(0, 0, 4, 2)]

with open("shapes.pkl", 'wb') as file:
    pickle.dump(shapes, file)

# Загрузка фигур из файла
with open("shapes.pkl", 'rb') as file:
    loaded_shapes = pickle.load(file)

# Отображение информации о фигурах
for shape in loaded_shapes:
    print(f"Shape Type: {type(shape).__name__}")
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    print()
