from random import choice, randrange as rr
from typing import Self


class Cat:
    names = ('Белка', 'Черныш', 'Рыжик', 'Мурзя', 'Черепаха')
    colors = ('чёрный', 'белый', 'рыжий', 'серый', 'пятнистый', 'черепаховый')
    hunter = 81
    
    # special, dunder, специальные, встроенные, "магические"
    def __init__(self, name: str = None):
        if name is None:
            name = choice(self.names)
        self.name = name
        self.color = choice(self.colors)
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}, окрас: {self.color}>'
    
    def __str__(self):
        return f'{self.name}'
    
    @staticmethod
    def meow() -> str:
        return 'мяу'
    
    def hungry(self) -> str:
        return '-'.join(self.meow() for _ in range(rr(2, 5)))
    
    def hunt(self) -> bool:
        """"""
        res = choice([True]*self.hunter + [False]*(100-self.hunter))
        print('охота удалась' if res else 'неудача')
        return res
    
    @classmethod
    def reproduce(cls) -> list[Self]:
        return [cls() for _ in range(rr(2, 6))]


yara = Cat('Яра')

# >>> Cat.hunt
# <function Cat.hunt at 0x0000028391F7FBA0>

# >>> yara.hunt
# <bound method Cat.hunt of <__main__.Cat object at 0x0000028391F80B90>>

# вызов метода yara.hunt() подменяется вызовом функции Cat.hunt(yara)
yara.hunt()

# для всех связанных методов:
# self.method(*args, **kwargs)
#     |
#     V
# self.__class__.function(self, *args, **kwargs)



# >>> Cat.meow
# <function Cat.meow at 0x000001B08C4D5620>

# >>> yara.meow
# <function Cat.meow at 0x000001B08C4D5620>

# при вызове статического метода подмена не осуществляется, вызывается объект функции
yara.meow()

# для всех статических методов:
# self.static_method(*args, **kwargs)
#     |
#     V
# self.__class__.static_method(*args, **kwargs)



# >>> Cat.reproduce
# <bound method Cat.reproduce of <class '__main__.Cat'>>

# >>> yara.reproduce
# <bound method Cat.reproduce of <class '__main__.Cat'>>

# вызов классового метода yara.reproduce() подменяется вызовом reproduce(Cat)
yara.reproduce()

# для всех классовых методов:
# self.class_method(*args, **kwargs)
#     |
#     V
# class_method(self.__class__, *args, **kwargs)

# вызов классового метода Cat.reproduce() подменяется вызовом reproduce(Cat)
Cat.reproduce()

# для всех классовых методов:
# cls.class_method(*args, **kwargs)
#     |
#     V
# class_method(cls, *args, **kwargs)


