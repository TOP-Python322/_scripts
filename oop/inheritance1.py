class Base:
    """
    Базовый(/родительский/над-) класс.
    """
    cls_attr1 = 10

    def __init__(self):
        print('конструктор базового класса')
        self.inst_attr1 = 'abc'

    def check(self) -> bool:
        return bool(self.inst_attr1)


class Subclass(Base):
    """
    Производный(/дочерний/под-) класс.
    """


# >>> bc1 = Base()
# >>> конструктор базового класса
# >>>
# >>> bc1.new_attr = (-0.1, 0.1)
# >>> bc1.__dict__
# {'inst_attr1': 'abc', 'new_attr': (-0.1, 0.1)}
# >>>
# >>> Subclass.__init__
# <function Base.__init__ at 0x000002193FE11B20>
# >>>
# >>> sc1 = Subclass()
# конструктор базового класса
# >>>
# >>> sc1.cls_attr1
# 10
# >>> sc1.inst_attr1
# 'abc'
# >>>
# >>> sc1.__dict__
# {'inst_attr1': 'abc'}
# >>>
# >>> sc1.check()
# True

