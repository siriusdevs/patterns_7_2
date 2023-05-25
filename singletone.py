# Написать класс PersonAttrsCreator, объект которого имеет два метода: 
# age() -> int возвращает случайный возраст от 0 до 100 
# name() -> str возвращает случайное имя 
# (можно использовать любой набор букв, где первая - заглавная, а можно использовать faker) 
# Использовать паттерн Синглтон (Singleton), 
# чтобы при работе программы всегда создавался только один экземпляр класса PersonAttrsCreator.

from random import randint
from faker import Faker

class PersonAttrsCreator:

    def age() -> int:
        return randint(0, 100)
    
    def name(self) -> str:
        return Faker(self.name)
    
class Singletone():

    def create(cls):
        return PersonAttrsCreator
    
    # def create():
    #     return PersonAttrsCreator

person = Singletone()
person.create()
print(person.create)