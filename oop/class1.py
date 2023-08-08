class User:
    username: str
    password: str
    email: str
    
    def auth(self, input_password: str):
        ...


ivan = User()
ivan.username = 'ivannnnn9000'
ivan.password = '12345'

anna = User()
anna.username = 'anutka2002'
anna.password = 'qwerty'


# объект класса
# >>> User
# <class '__main__.User'>

# объекты экземпляров
# >>> ivan
# <__main__.User object at 0x0000023AF25408D0>
# >>> anna
# <__main__.User object at 0x0000023AF2540A50>

# ссылки на объект класса в экземпляре
# >>> type(ivan)
# <class '__main__.User'>
# >>>
# >>> ivan.__class__
# <class '__main__.User'>
# >>>
# >>> type(ivan) is ivan.__class__ is User
# True

# базовые типы — это тоже классы
# >>> text = 'строка'
# >>>
# >>> type(text)
# <class 'str'>
# >>>
# >>> text.__class__
# <class 'str'>
# >>>
# >>> type(text) is text.__class__ is str
# True