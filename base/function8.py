def test():
    """Демонстратор объекта функции."""


print(f'{type(test)}\n{test}')
print(test.__name__)
print(test.__doc__)

new_func = test

print(f'{type(new_func)}\n{new_func}')
print(new_func.__name__)
print(new_func.__doc__)

del test

# >>> test
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# NameError: name 'test' is not defined
# >>>
# >>> new_func
# <function test at 0x0000026397952D40>
