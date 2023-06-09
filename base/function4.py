var1 = 'какой-то там текст'
var2 = 5200
var3 = {'a': 10, 'b': 20, 'c': 30}


def some_func(var1):
    var2 = [(0.01, 'z'), (0.03, 'b')]
    print(f'внутри функции some_func:\n{var1 = } {var2 = }\n')


print(f'снаружи функции до вызова:\n{var1 = } {var2 = }\n')
some_func('совсем другой текст')
print(f'снаружи функции после вызова:\n{var1 = } {var2 = }\n')


def other_func(numbers: list[int]):
    print(f'внутри функции other_func:\n{var1 = } {var2 = }\n')
    # приведёт к UnboundLocalError
    # var2 = 100
    
    # приведёт к UnboundLocalError
    # var3 = {0.1: 'abc'}
    
    # изменение возможно для изменяемых объектов
    var3['a'] = 1000
    
    print(f'{id(numbers) = }')
    
    numbers.append(0)
    numbers.insert(0, 0)


test_nums = list(range(10, 100, 10))
print(f'{id(test_nums) = }')

other_func(test_nums)
print(f'после вызова other_func:\n{var3 = } {test_nums = }\n')

