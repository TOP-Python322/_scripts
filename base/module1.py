"""
Главный модуль — точка входа.
"""
print('начало выполнения главного модуля', end='\n\n')

# для собственных модулей проекта
import module2
# для модулей стандартной и внешних библиотек
from module2 import b_str, b_list

a = 100

print({k: v for k, v in locals().items() if not k.startswith('__')}, end='\n\n')

print(f'{module2.b = }')
module2.b += 22
print(f'{module2.b = }', end='\n\n')

print(f'{module2.module3.c = }')
module2.module3.c += 33
print(f'{module2.module3.c = }', end='\n\n')

b_str = 'переменная главного модуля'
b_list += ['o', 'p']

print(f'{module2.b_str = }')
print(f'{module2.b_list = }', end='\n\n')

print('конец выполнения главного модуля', end='\n\n')