from re import compile
from typing import Literal


class Person:
    _pat_name = compile(r'[А-ЯЁ][а-яё]+(-[А-ЯЁ][а-яё]+)?')

    def __init__(self, last_name: str, first_name: str, patr_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.__fio = f'{last_name} {first_name} {patr_name}'
    
    @property
    def fio(self) -> str:
        return self.__fio
    
    # сеттер для атрибутов last_name, first_name и patr_name
    def change_name(self, new_name: str, name_type: Literal['last', 'first', 'patr']):
        if self._pat_name.fullmatch(new_name):
            setattr(self, f'{name_type}_name', new_name)
            self.__fio = f'{self.last_name} {self.first_name} {self.patr_name}'
    
    def __repr__(self):
        return self.fio
    
    def __str__(self):
        return self.__repr__()



people = [
    Person('Агафонов', 'Ануфрий', 'Проклович'),
    Person('Северов', 'Пармен', 'Ерофеевич'),
    Person('Кожевников', 'Прокоп', 'Августович'),
]

# >>> for p in people:
# ...     print(p)
# ...
# Агафонов Ануфрий Проклович
# Северов Пармен Ерофеевич
# Кожевников Прокоп Августович

# >>> people[0].fio = 'A B C'
# ...
# AttributeError: property 'fio' of 'Person' object has no setter

# >>> for p in people:
# ...     p.change_name('Иван', 'first')
# ...
# >>> print(*(p.fio for p in people), sep='\n')
# Агафонов Иван Проклович
# Северов Иван Ерофеевич
# Кожевников Иван Августович

