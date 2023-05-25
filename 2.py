# Написать класс PersonAttrsCreator, объект которого имеет два метода: 
# age() -> int возвращает случайный возраст от 0 до 100 
# name() -> str возвращает случайное имя 
# (можно использовать любой набор букв, где первая - заглавная, а можно использовать faker) 
# Использовать паттерн Синглтон (Singleton), 
# чтобы при работе программы всегда создавался только один экземпляр класса PersonAttrsCreator.
from random import randint, choice
from string import ascii_lowercase as lowcase

class PersonAttrsCreator:
    def age(self) -> int:
        return randint(0,100)

    def name(self) -> str:
        name = ''
        for _ in range(randint(5, 12)):
            letter = choice(lowcase)
            name += letter
        return name.capitalize()