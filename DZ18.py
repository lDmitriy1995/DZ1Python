class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} is turned on.")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turned off.")

class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"Making {self.coffee_type} coffee with {self.brand} {self.model}.")

class Blender(Device):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def blend(self):
        print(f"Blending with {self.brand} {self.model} ({self.capacity}L).")

class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        print(f"Grinding meat with {self.brand} {self.model} ({self.power}W).")



class Ship:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start_engine(self):
        print(f"{self.name} engine started.")

    def stop_engine(self):
        print(f"{self.name} engine stopped.")

class Frigate(Ship):
    def __init__(self, name, year, missile_count):
        super().__init__(name, year)
        self.missile_count = missile_count

    def launch_missile(self):
        print(f"Launching {self.missile_count} missiles from {self.name}.")

class Destroyer(Ship):
    def __init__(self, name, year, cannon_count):
        super().__init__(name, year)
        self.cannon_count = cannon_count

    def fire_cannons(self):
        print(f"Firing {self.cannon_count} cannons from {self.name}.")

class Cruiser(Ship):
    def __init__(self, name, year, missile_system):
        super().__init__(name, year)
        self.missile_system = missile_system

    def launch_missile_system(self):
        print(f"Launching missile system ({self.missile_system}) from {self.name}.")



class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display(self):
        print(f"${self.dollars}.{self.cents:02}")

    def set_value(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add(self, dollars, cents):
        self.dollars += dollars
        self.cents += cents
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents %= 100

    def subtract(self, dollars, cents):
        self.dollars -= dollars
        self.cents -= cents
        if self.cents < 0:
            self.dollars -= abs(self.cents) // 100 + 1
            self.cents = 100 - abs(self.cents) % 100

# Примеры использования классов

if __name__ == "__main__":
    # Пример использования классов Device и его наследников
    coffee_machine = CoffeeMachine("BrandX", "ModelA", "Espresso")
    blender = Blender("BrandY", "ModelB", 2)
    meat_grinder = MeatGrinder("BrandZ", "ModelC", 500)

    coffee_machine.turn_on()
    coffee_machine.make_coffee()

    blender.turn_on()
    blender.blend()

    meat_grinder.turn_on()
    meat_grinder.grind_meat()

    # Пример использования классов Ship и его наследников
    frigate = Frigate("Frigate1", 2022, 8)
    destroyer = Destroyer("Destroyer2", 2019, 16)
    cruiser = Cruiser("Cruiser3", 2020, "Tomahawk")

    frigate.start_engine()
    frigate.launch_missile()

    destroyer.start_engine()
    destroyer.fire_cannons()

    cruiser.start_engine()
    cruiser.launch_missile_system()

    # Пример использования класса Money
    money = Money(50, 75)
    money.display()

    money.add(25, 30)
    money.display()

    money.subtract(20, 50)
    money.display()


