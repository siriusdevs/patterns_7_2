# Написать класс PersonAttrsCreator, объект которого имеет два метода:
# age() -> int возвращает случайный возраст от 0 до 100
# name() -> str возвращает случайное имя
# (можно использовать любой набор букв, где первая - заглавная, а можно использовать faker)
# Использовать паттерн Синглтон (Singleton),
# чтобы при работе программы всегда создавался только один экземпляр класса PersonAttrsCreator.

from random import randint

from faker import Faker


class Singleton:
    __object = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__object, cls):
            cls.__object = object.__new__(cls)
        return cls.__object


class PersonAttrsCreator:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def age() -> int:
        return randint(0, 100)

    def name() -> str:
        return Faker()
