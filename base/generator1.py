def generator_func():
    print('начало вычисления тела генераторной функции')
    print('первая итерация:', end=' ')
    yield 1
    print('вторая итерация:', end=' ')
    yield 2
    print('конец вычисления тела генераторной функции')


generator_obj = generator_func()
print(f'{type(generator_obj)}\n{generator_obj}\n')

print(generator_obj.__next__())
print(generator_obj.__next__())
try:
    print(generator_obj.__next__())
except StopIteration:
    pass

# по объекту генератора можно проитерироваться только единожды
print(list(generator_obj))

generator_obj = generator_func()
print(list(generator_obj))

# не выведет ничего — StopIteration перехватывает сам цикл for
for n in generator_obj:
    print(n)
