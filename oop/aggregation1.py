from datetime import date, timedelta as td
from itertools import chain
from typing import Literal


class Product:
    def __init__(self, name: str, long: td, produced: date = None):
        self.name = name
        if produced is None:
            produced = date.today()
        self.produced = produced
        self.expired: date = produced + long
    
    def __repr__(self):
        return f'<{self.name!r}: {self.produced:%d.%m.%y}–{self.expired:%d.%m.%y}>'


class Fridge:
    def __init__(self):
        self._cold: list[Product] = []
        self.__freezer: list[Product] = []
    
    def __repr__(self):
        return '\n'.join(repr(pr) for pr in chain(self._cold, self.__freezer))
    
    def add_product(self, *products: Product, box: Literal['c', 'f'] = 'c') -> None:
        if box == 'c':
            box = self._cold
        elif box == 'f':
            box = self.__freezer
        else:
            raise ValueError
        box.extend(products)

    def clear_expired(self) -> None:
        today = date.today()
        for product in self._cold:
            if not product.produced <= today <= product.expired:
                self._cold.remove(product)
        for product in self.__freezer:
            if not product.produced <= today <= product.expired:
                self.__freezer.remove(product)


fr1 = Fridge()
fr1.add_product(
    Product('молоко', td(days=7), date(2023, 8, 14)),
    Product('сметана', td(days=14)),
    Product('сливки', produced=date(2023, 8, 15), long=td(days=30)),
    box='c'
)
fr1.add_product(
    Product('говядина замороженная', produced=date(2023, 8, 2), long=td(days=90)),
    Product('минтай замороженный', produced=date(2023, 7, 20), long=td(days=70)),
    box='f'
)

