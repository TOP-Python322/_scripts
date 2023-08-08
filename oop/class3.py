class Keyboard:
    # атрибуты класса
    keys: int = 105
    
    # конструктор
    def __init__(self) -> None:
        # атрибуты экземпляра
        self.numlock: bool = True
        self.capslock: bool = False
        self.scrolllock: bool = False


# во время создания экземпляра вызывается метод __init__ — конструктор
agh_1000 = Keyboard()
hp_wireless2 = Keyboard()

# во время вызовы объекта класса вызывается следующая функция:
# def __call__(...) -> Keyboard:
    # шаг 1. создание "чистого" экземпляра
    # instance = __new__(Keyboard)
    # шаг 2. настройка экземпляра
    # Keyboard.__init__(instance)
    # шаг 3. возврат экземпляра
    # return instance


# внутренне пространство имён класса
# >>> print(*Keyboard.__dict__, sep='\n')
# __module__
# __annotations__
# keys
# __init__
# __dict__
# __weakref__
# __doc__

# внутренне пространство имён экземпляра
# >>> agh_1000.__dict__
# {'numlock': True, 'capslock': False, 'scrolllock': False}
# >>>
# >>> hp_wireless2.__dict__
# {'numlock': True, 'capslock': False, 'scrolllock': False}
