# Написать следующую структуру классов: 
# Абстрактное транспортное средство Vehicle, у которого есть: 

# Свойства: 
# surface: str - вид поверхности, по которому оно передвигается 
# speed: int - скорость транспортного средства 

# Методы: 
# move() -> None - метод, который выводит через print, по какой поверхности и с какой скоростью оно передвигается 
# set_surface(surface:str) -> None - устанавливает тип поверхности для передвижения 
# set_speed(speed: int) -> None - устанавливает скорость транспортного средства. 

# Использовать паттерн Строитель (Builder) и написать классы 
# VehicleBuilder (абстрактный), BoatBuilder (строит лодку), CarBuilder (строит машину). 
# У всех строителей есть метод create(speed: int) -> Vehicle. 

from abc import ABC

class Vehicle(ABC):
    surface: str
    speed: int

    def __init__(self, speedd: int = 0, surfacee: str=None):
        self.surfacee = surfacee
        self.speedd = speedd

    def move(self) -> None:
        print(f'Транспортное средство передвигается по:{self.surfacee}')

    def set_surface(self, surface:str) -> None:
        self.surfacee = surface

    def set_speed(self, speed: int) -> None:
        self.speedd = speed

class VehicleBuilder(ABC):
    def create(veh_type, speed) -> Vehicle:
        return Vehicle(veh_type, speed)

class BoatBuilder(Vehicle):
    def create(speed: int) -> Vehicle:
        boat = VehicleBuilder('Water', speed)

class CarBuilder(Vehicle):
    def create(speed: int) -> Vehicle:
        VehicleBuilder('Ground', speed)


vb = VehicleBuilder()
print(vb.create(BoatBuilder()))
