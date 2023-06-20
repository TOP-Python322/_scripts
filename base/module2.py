"""
Дополнительный модуль 2.
"""
print('\tначало выполнения модуля 2', end='\n\n')

import module3

b = 200

b_str = 'переменная модуля 2'
b_list = ['m', 'n']

print('\t', {k: v for k, v in locals().items() if not k.startswith('__')}, end='\n\n')

print('\tконец выполнения модуля 2', end='\n\n')