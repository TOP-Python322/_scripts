class Keyboard:
    # атрибуты класса
    keys: int = 105
    
    numlock: bool = True
    capslock: bool = False
    scrolllock: bool = False



agh_1000 = Keyboard()
# создание атрибута экземпляра
agh_1000.volume = 50

hp_wireless2 = Keyboard()


# все экземпляры имеют доступ к атрибутам класса
# >>> agh_1000.keys
# 105
# >>> hp_wireless2.keys
# 105

# >>> agh_1000.volume
# 50
# внутреннее пространство имён экземпляра
# >>> agh_1000.__dict__
# {'volume': 50}

# атрибут volume не определён
# >>> hp_wireless2.volume
# ...
# AttributeError: 'Keyboard' object has no attribute 'volume'
# >>>
# >>> hp_wireless2.__dict__
# {}

# внутреннее пространство имён класса
# >>> print(*Keyboard.__dict__.items(), sep='\n')
# ('__module__', '__main__')
# ('__annotations__', {'keys': <class 'int'>, 'numlock': <class 'bool'>, 'capslock': <class 'bool'>, 'scrolllock': <class 'bool'>})
# ('keys', 105)
# ('numlock', True)
# ('capslock', False)
# ('scrolllock', False)
# ('__dict__', <attribute '__dict__' of 'Keyboard' objects>)
# ('__weakref__', <attribute '__weakref__' of 'Keyboard' objects>)
# ('__doc__', None)

# область видимости, расширенная до объекта класса
# >>> print(*agh_1000.__dir__(), sep='\n')
# volume
# __module__
# __annotations__
# keys
# numlock
# capslock
# scrolllock
# __dict__
# __weakref__
# __doc__
# ...
