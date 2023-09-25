# Класс Device
class Device:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def turn_on(self):
        pass

    def turn_off(self):
        pass

# Класс CoffeeMachine наследует от Device
class CoffeeMachine(Device):
    def __init__(self, name, brand, coffee_type):
        super().__init__(name, brand)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"Making {self.coffee_type} coffee")

# Класс Blender наследует от Device
class Blender(Device):
    def __init__(self, name, brand, capacity):
        super().__init__(name, brand)
        self.capacity = capacity

    def blend(self):
        print(f"Blending with {self.capacity} capacity")

# Класс MeatGrinder наследует от Device
class MeatGrinder(Device):
    def __init__(self, name, brand, power):
        super().__init__(name, brand)
        self.power = power

    def grind_meat(self):
        print(f"Grinding with {self.power} power")

# Класс Ship
class Ship:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def sail(self):
        pass

# Класс Frigate наследует от Ship
class Frigate(Ship):
    def __init__(self, name, country, num_guns):
        super().__init__(name, country)
        self.num_guns = num_guns

    def fire_guns(self):
        print(f"Firing {self.num_guns} guns")

# Класс Destroyer наследует от Ship
class Destroyer(Ship):
    def __init__(self, name, country, num_missiles):
        super().__init__(name, country)
        self.num_missiles = num_missiles

    def launch_missiles(self):
        print(f"Launching {self.num_missiles} missiles")

# Класс Cruiser наследует от Ship
class Cruiser(Ship):
    def __init__(self, name, country, num_cannons):
        super().__init__(name, country)
        self.num_cannons = num_cannons

    def fire_cannons(self):
        print(f"Firing {self.num_cannons} cannons")

# Класс Money
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display_amount(self):
        print(f"{self.dollars} dollars and {self.cents} cents")

    def set_amount(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

# Пример использования классов

coffee_machine = CoffeeMachine("CoffeeMaster", "BrandX", "Espresso")
coffee_machine.turn_on()
coffee_machine.make_coffee()
coffee_machine.turn_off()

blender = Blender("SuperBlender", "BrandY", "1.5L")
blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder = MeatGrinder("MeatMuncher", "BrandZ", "500W")
meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.turn_off()

frigate = Frigate("FrigateA", "CountryX", 12)
frigate.sail()
frigate.fire_guns()

destroyer = Destroyer("DestroyerB", "CountryY", 20)
destroyer.sail()
destroyer.launch_missiles()

cruiser = Cruiser("CruiserC", "CountryZ", 8)
cruiser.sail()
cruiser.fire_cannons()

money = Money(100, 50)
money.display_amount()
money.set_amount(200, 75)
money.display_amount()
