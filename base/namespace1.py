line = '='*5
print(f'\n {line} глобальное пространство имён {line} \n')

a = 1
var1 = 'xyz'

print(globals(), end='\n\n')

def test_func():
    # global var1
    print(f'\n {line} локальное пространство имён {line} \n')
    a = ['PP', 'YY']
    sum = 123
    print(f'{a=}', end='\n\n')
    print(f'{var1=}', end='\n\n')
    # var1 = '9'
    print(globals(), end='\n\n')
    print(locals(), end='\n\n')

print(f'\n {line} глобальное пространство имён {line} \n')

test_func()

print(f'\n {line} глобальное пространство имён {line} \n')

print(locals())
