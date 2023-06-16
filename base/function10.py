def filter(predicate: 'function', iterable: 'iterable') -> list:
    """Вызывает predicate для каждого элемента iterable. Возвращает те элементы iterable, для которых возвращаемое значение функции-предиката истинно.
    
    В predicate передаётся в качестве аргумента один объект — элемент iterable."""
    result = []
    for elem in iterable:
        if predicate(elem):
            result += [elem]
    return result


objects = [90, '12', 34, '67', '2', 31]
numbers = filter(lambda elem: isinstance(elem, int), objects)
print(numbers)


float_chars = set('0123456789.')

def is_floatable(string: str) -> bool:
    try:
        return (
                set(string[1:]) <= float_chars 
            and set(string[0]) <= float_chars | {'-'}
        )
    except IndexError:
        return False


inputs = ['12', '.34', '5.6', '78.', 'abc', '-9', '-10.', '-1.1', '-.12', '13-1']
numbers = [float(inp) for inp in filter(is_floatable, inputs)]
print(numbers)
