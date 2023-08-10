from random import choice


class Cat:
    names = ('Белка', 'Черныш', 'Рыжик', 'Мурзя', 'Черепаха')
    hunter = 81
    
    # special, dunder, специальные, встроенные, "магические"
    def __init__(self, name: str = None):
        if name is None:
            name = choice(self.names)
        self.name = name
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'
    
    def __str__(self):
        return f'{self.name}'
    
    def hunt(self) -> bool:
        """"""
        res = choice([True]*self.hunter + [False]*(100-self.hunter))
        print('охота удалась' if res else 'неудача')
        return res


yara = Cat('Яра')

# >>> Cat.hunt
# <function Cat.hunt at 0x0000028391F7FBA0>

# >>> yara.hunt
# <bound method Cat.hunt of <__main__.Cat object at 0x0000028391F80B90>>

# вызов метода yara.hunt() подменяется вызовом функции Cat.hunt(yara)
yara.hunt()

# self.method(*args, **kwargs)
#     |
#     V
# self.__class__.function(self, *args, **kwargs)


