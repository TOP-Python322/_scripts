def map(function: 'function', iterable: 'iterable') -> list:
    """Вызывает function для каждого элемента iterable. Возвращает список возвращаемых значений function.
    
    В function передаётся в качестве аргумента один объект — элемент iterable."""
    result = []
    for elem in iterable:
        result += [function(elem)]
    return result


numbers = map(int, '0123456789')
print(numbers)


def anti_abs(number: float) -> float:
    """Анти-модуль числа: всегда возвращает отрицательное число."""
    return -number if number > 0 else number


negatives = map(anti_abs, range(-5, 6))
print(negatives)


square_roots = map(lambda x: x**0.5, range(10, 50))
print(square_roots)


def adder(x, y=1):
    return x + y


numbers = map(adder, range(10))
print(numbers)
