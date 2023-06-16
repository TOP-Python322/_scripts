from time import perf_counter


def elapser(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        end = perf_counter()
        print(f'Время выполнения: {end-start:.6f}')
        return result
    return wrapper


@elapser
def product(numbers: 'iterable') -> float:
    if 0 in numbers:
        return 0.0

    result = 1.0
    for n in numbers:
        result *= n
    return result


@elapser
def vector_sum(vector1: list[float], vector2: list[float]) -> list[float]:
    result = []
    n, m = len(vector1), len(vector2)
    for i in range(max(n, m)):
        try:
            v1 = vector1[i]
        except IndexError:
            v1 = 0
        try:
            v2 = vector2[i]
        except IndexError:
            v2 = 0
        result += [float(v1 + v2)]
    return result


print(product(range(1, 100, 3)))
print(product(range(1, 1500, 3)), end='\n\n')


vector1 = range(20)
vector2 = range(10, 100, 3)
print(f'{len(vector1) = }\t{len(vector2) = }')

vector3 = vector_sum(vector1, vector2)
print(f'{len(vector3) = }\n{vector3}')
