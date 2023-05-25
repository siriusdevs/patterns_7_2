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

from abc import ABC, abstractmethod

class Vehicle(ABC):
    surface : str
    speed : int

    def __init__(self, surface: str, speed: int):
        self.surface = surface
        self.speed = speed

    def move() -> None:
        print(f'Vehicle move on {Vehicle.surface}, with speed {Vehicle.speed}')

    def set_speed(speed: int) -> None:
        new_speed = speed + 10
        return new_speed

    def set_surface(surface: str):
        new_surface = 'Асфальт'
        return new_surface

class Builder:
    def create(speed: int, surface: str) -> Vehicle:
        return f'Transport\'s speed {speed}, and surface {surface}'


class VehicleBuilder(Vehicle, Builder):
    pass

class BoatBuilder(Builder):
    pass

class CarBuilder(Builder):
    pass


vehicle_1 = VehicleBuilder('ground', 15)
vehicle_1.move()

vehicle_2 = VehicleBuilder()
print(vehicle_2)

boat = BoatBuilder()
print(boat)

car = CarBuilder()
print(car)