from json import loads
from pathlib import Path
from sys import path


data_path = Path(path[0]) / '_Natural.json'


# Natural()
# в метаклассе:
# def __call__(cls, ...):
#     instance = cls.__new__(...)
#     instance.__init__(...)
#     return instance

class Natural:
    """
    Натуральное число в диапазоне от 1 до 999.
    
    Если результатом математической операции является не натуральное число, то будет возвращён экземпляр int или float.
    
    Человекочитаемое строковое представление является числительным.
    """
    __numerals = {
        int(k): v
        for k, v in loads(data_path.read_text(encoding='utf-8')).items()
    }
    
    def __new__(cls, number: int):
        if 0 < number < 1000:
            instance = object.__new__(cls)
        else:
            return number
        
        instance.__value = number
        
        tens_ones = cls.__numerals.get(number%100, None)
        if tens_ones:
            hundreds = cls.__numerals.get(number//100*100)
            if hundreds:
                instance.__str = f'{hundreds} {tens_ones}'
            else:
                instance.__str = f'{tens_ones}'
        else:
            ranks, i = [], 0
            while number:
                number, rem = divmod(number, 10)
                ranks.append(rem*10**i)
                i += 1
            instance.__str = ' '.join(cls.__numerals.get(n, '') for n in ranks[::-1])
        
        return instance
    
    # можно реализовать геттер и сеттер для __value, чтобы явно сообщить пользователю о неизменяемости данного объекта
    
    # @property
    # def value(self):
        # raise NotImplementedError
    
    # @value.setter
    # def value(self, new_value):
        # raise NotImplementedError
    
    def __repr__(self):
        return self.__value.__repr__()
    
    def __str__(self):
        return self.__str
    
    def __int__(self):
        return self.__value
    
    def __index__(self):
        return self.__value - 1
    
    # n1 < n2 --> n1.__lt__(n2)
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__value < other.__value
        elif isinstance(other, (int, float)):
            return self.__value < other
        else:
            raise TypeError('')
    
    # ...
    
    # n1 + n2 --> n1.__add__(n2)
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Natural(self.__value + other.__value)
        elif isinstance(other, int):
            return Natural(self.__value + other)
        elif isinstance(other, float):
            return self.__value + other
        else:
            raise TypeError('')
    
    # 23 + n1 --> n1.__radd__(23)
    def __radd__(self, other):
        return self.__add__(other)
    
    # n1 += n2 --> n1 = n1.__iadd__(n2)
    def __iadd__(self, other):
        return self.__add__(other)
    
    # -n1 --> n1.__neg__()
    def __neg__(self) -> int:
        return -self.__value
    
    # n1 - n2 --> n1.__sub__(n2)
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Natural(self.__value - other.__value)
        elif isinstance(other, int):
            return Natural(self.__value - other)
        elif isinstance(other, float):
            return self.__value - other
        else:
            raise TypeError('')
    
    # 10 - n1 --> n1.__rsub__(10)
    def __rsub__(self, other):
        if isinstance(other, self.__class__):
            return Natural(other.__value - self.__value)
        elif isinstance(other, int):
            return Natural(other - self.__value)
        elif isinstance(other, float):
            return other - self.__value
        else:
            raise TypeError('')
    
    # n1 -= n2 --> n1 = n1.__sub__(n2)
    def __isub__(self, other):
        return self.__sub__(other)
    
    # ...
    
    # n1 / n2 --> n1.__truediv__(n2)
    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return self.__value / other.__value
        elif isinstance(other, (int, float)):
            return self.__value / other
        else:
            raise TypeError('')
    
    # ...


n1 = Natural(5)
n2 = Natural(9)
