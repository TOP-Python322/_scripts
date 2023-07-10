from itertools import chain, zip_longest
from string import ascii_lowercase


iterator = chain(range(10), ascii_lowercase)

print(f'\n{type(iterator)}\n{iterator}\n')

for elem in iterator:
    print(elem, end=' ')
print()


numbers = range(2, 9)
letters = 'MNXYZ'
print('\nzip (built-in)')
for elem in zip(numbers, letters):
    print(elem)

print('\nzip_longest')
for elem in zip_longest(numbers, letters, fillvalue=''):
    print(elem)
