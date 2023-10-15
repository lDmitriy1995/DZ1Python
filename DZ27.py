class Vehicle:
    def __init__(self, vehicle_type):
        self.type = vehicle_type

    def get_type(self):
        return self.type

    def __repr__(self):
        return f"Vehicle({self.type})"

    def __str__(self):
        return f"Type: {self.type}"

class Bus:
    def __init__(self, bus_number):
        self.number = bus_number

    def get_number(self):
        return self.number

    def __repr__(self):
        return f"Bus {self.number}"

    def __str__(self):
        return f"Bus Number: {self.number}"

class BusSchedule:
    def __init__(self):
        self.schedule = []

    def add_bus(self, bus_number, departure_time):
        self.schedule.append((bus_number, departure_time))

    def get_schedule(self):
        return self.schedule

    def get_schedule_by_bus_number(self, bus_number):
        return [(bus, time) for bus, time in self.schedule if bus == bus_number]

    def is_bus(self, vehicle_number):
        return isinstance(vehicle_number, Bus)

    def check_schedule(self, bus_number, departure_time):
        return (bus_number, departure_time) in self.schedule

# Пример использования:
if __name__ == "__main__":
    v = Vehicle("Car")
    print(v.get_type())
    print(repr(v))
    print(str(v))

    b = Bus("101")
    print(b.get_number())
    print(repr(b))
    print(str(b))

    schedule = BusSchedule()
    schedule.add_bus("101", "10:00")
    schedule.add_bus("102", "11:00")
    print(schedule.get_schedule())
    print(schedule.get_schedule_by_bus_number("101"))
    print(schedule.is_bus(b))
    print(schedule.check_schedule("101", "10:00"))





import unittest
from VehicleClass import Vehicle, Bus, BusSchedule

class TestVehicle(unittest.TestCase):

    def test_get_type(self):
        vehicle = Vehicle("Car")
        self.assertEqual(vehicle.get_type(), "Car")

    def test_str_and_repr(self):
        vehicle = Vehicle("Bike")
        self.assertEqual(str(vehicle), "Type: Bike")
        self.assertEqual(repr(vehicle), "Vehicle(Bike)")

    def test_instance_of_vehicle(self):
        vehicle = Vehicle("Truck")
        self.assertIsInstance(vehicle, Vehicle)

class TestBus(unittest.TestCase):

    def test_get_number(self):
        bus = Bus("123")
        self.assertEqual(bus.get_number(), "123")

    def test_str_and_repr(self):
        bus = Bus("456")
        self.assertEqual(str(bus), "Bus Number: 456")
        self.assertEqual(repr(bus), "Bus 456")

    def test_instance_of_bus(self):
        bus = Bus("789")
        self.assertIsInstance(bus, Bus)

class TestBusSchedule(unittest.TestCase):

    def test_add_bus(self):
        schedule = BusSchedule()
        schedule.add_bus("101", "10:00")
        self.assertIn(("101", "10:00"), schedule.get_schedule())

    def test_get_schedule_by_bus_number(self):
        schedule = BusSchedule()
        schedule.add_bus("201", "08:00")
        schedule.add_bus("202", "09:00")
        self.assertEqual(schedule.get_schedule_by_bus_number("201"), [("201", "08:00")])

    def test_is_bus(self):
        schedule = BusSchedule()
        self.assertTrue(schedule.is_bus(Bus("301")))
        self.assertFalse(schedule.is_bus(Vehicle("Car")))

    def test_check_schedule(self):
        schedule = BusSchedule()
        schedule.add_bus("401", "12:00")
        schedule.add_bus("402", "13:00")
        self.assertTrue(schedule.check_schedule("401", "12:00"))
        self.assertFalse(schedule.check_schedule("401", "13:00"))
        with self.assertRaises(ValueError):
            schedule.check_schedule("403", "12:00")

if __name__ == '__main__':
    unittest.main()

