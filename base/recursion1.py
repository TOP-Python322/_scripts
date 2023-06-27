def counter(start: int):
    if start > 0:
        print(f'перед рекурсивным вызовом, {start=}')
        result = counter(start-1)
        print(f'после рекурсивного вызова, {result=}')
        return result
    else:
        print(f'последний вызов, {start=}')
        return start


