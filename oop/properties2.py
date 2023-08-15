class Square:
    def __init__(self, side: float):
        self.side = side
        self.area = side**2


# >>> sq1 = Square(5)
# >>> sq1.side
# 5
# >>> sq1.area
# 25
# >>>
# >>> sq1.side = 7
# >>> sq1.area
# 25



class Square:
    def __init__(self, side: float):
        self.__side = side
        self.__area = side**2
    
    # геттер для атрибута __side
    @property
    def side(self) -> float:
        return self.__side
    
    # сеттер для атрибута __side
    @side.setter
    def side(self, new_side: float) -> None:
        self.__area = new_side**2
        self.__side = new_side
    
    # геттер для атрибута __area
    @property
    def area(self) -> float:
        return self.__area
    
    # сеттер для атрибута __area
    @area.setter
    def area(self, new_area: float) -> None:
        self.__side = new_area**0.5
        self.__area = new_area


# >>> sq1 = Square(4)
# >>>
# >>> sq1.__dict__
# {'_Square__side': 4, '_Square__area': 16}

# вызов геттера
# >>> sq1.side
# 4

# вызов геттера
# >>> sq1.area
# 16

# вызов сеттера
# >>> sq1.side = 11
# >>> sq1.area
# 121

# вызов сеттера
# >>> sq1.area = 81
# >>> sq1.side
# 9.0

