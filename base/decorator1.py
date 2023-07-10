from functools import wraps


def decorator(function):
    print('\tначало выполнения функции-декоратора')
    
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('\t\tначало выполнения функции-обёртки')
        result = function(*args, **kwargs)
        print('\t\tзавершение выполнения функции-обёртки')
        return result
    
    print('\tзавершение выполнения функции-декоратора')
    return wrapper


def test_func():
    """демонстратор декорируемой функции"""
    print('\t\t\tвыполнение декорируемой функции')


print(f'{test_func}\n{test_func.__name__}\n{test_func.__doc__}\n')
print('начало декорирования функции test_func')

test_func = decorator(test_func)

print('завершение декорирования функции test_func')
print(f'{test_func}\n{test_func.__name__}\n{test_func.__doc__}\n')

test_func()

print()


def adder(x, y):
    return x + y


adder = decorator(adder)
print(adder(3.5, 9), end='\n\n')


@decorator
def multiplier(x, y):
    return x * y

print(f'{multiplier}\n{multiplier.__name__}\n')
print(multiplier(1/3, 90))
