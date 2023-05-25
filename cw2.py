# Написать следующую структуру классов:
# Есть класс продукт, каждый продукт имеет свойства:
# name: str - имя,
# due_date : datetime (можно и другой формат) - срок годности.

# Используя паттерн компоновщик (Composite), написать класс Склад,
#  который имеет внутри скрытую коллекцию продуктов, умеет добавлять и удалять продукты внешними методами
#  add(product: Product) -> None и remove(product: Product) -> None,
#  а также 	имеет метод clean() -> None, который удаляет все просроченные продукты со склада.

from abc import ABC
from datetime import datetime
from typing import List


class Product:
    name: str
    due_date: datetime

    def __init__(self, name: str, due_date: datetime):
        self.name = name
        self.due_date = due_date

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name} in the shop with {self.due_date}'


class Composite:

    def __init__(self):
        self._products = []

    def add(self, product: Product):
        self._products.append(product)
        print(f'{product} was added')

    def remove(self, product: Product):
        if product in self._products:
            self._products.remove(product)
            print(f'{product} was removed')
        else:
            print(f'{product} was not found')

    def products(self):
        return self._products

    def clean(self):
        for product in self._products:
            if datetime.now() > product.due_date:
                self._products.remove(product)
                print(f'{product} was removed, because of due_date')


new_composite = Composite()
milk = Product('milk', datetime(2023, 9, 22))
chips = Product('chips', datetime(2023, 3, 22))
new_composite.add(milk)
new_composite.add(chips)
print([str(product) for product in new_composite.products()])
new_composite.remove(milk)
new_composite.clean()
print([str(product) for product in new_composite.products()])
