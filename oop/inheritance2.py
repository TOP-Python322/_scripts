class Proteus:
    @staticmethod
    def move():
        print('движение')

    @staticmethod
    def eat():
        print('питание')

    @staticmethod
    def reproduce():
        print('размножение')


class Fish(Proteus):
    @staticmethod
    def breath():
        print('дыхание')


class Reptile(Fish):
    @staticmethod
    def hide():
        print('скрытность')


class Bird(Reptile):
    @staticmethod
    def fly():
        print('полёт')


class Mammal(Reptile):
    @staticmethod
    def care():
        print('забота о потомстве')


class Human(Mammal):
    @staticmethod
    def speak():
        print('речь')


# >>> Proteus.__mro__
# (<class '__main__.Proteus'>, <class 'object'>)
# >>>
# >>> Fish.__mro__
# (<class '__main__.Fish'>, <class '__main__.Proteus'>, <class 'object'>)
# >>>
# >>> print(*Bird.__mro__, sep='\n')
# <class '__main__.Bird'>
# <class '__main__.Reptile'>
# <class '__main__.Fish'>
# <class '__main__.Proteus'>
# <class 'object'>
# >>>
# >>> print(*Human.__mro__, sep='\n')
# <class '__main__.Human'>
# <class '__main__.Mammal'>
# <class '__main__.Reptile'>
# <class '__main__.Fish'>
# <class '__main__.Proteus'>
# <class 'object'>


# >>> int
# <class 'int'>
# >>> int.__mro__
# (<class 'int'>, <class 'object'>)
# >>>
# >>> bool
# <class 'bool'>
# >>> bool.__mro__
# (<class 'bool'>, <class 'int'>, <class 'object'>)
