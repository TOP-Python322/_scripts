"""
Дополнительный модуль 3.
"""
print('\t\tначало выполнения модуля 3', end='\n\n')

c = 300

print('\t\t', {k: v for k, v in locals().items() if not k.startswith('__')}, end='\n\n')

print('\t\tконец выполнения модуля 3', end='\n\n')