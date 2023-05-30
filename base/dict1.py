test_dict = {'a': 1, 'b': 2, 'c': 3}

# for key in test_dict.keys():
for key in test_dict:
    print(key, end=' ')
print()

for value in test_dict.values():
    print(value, end=' ')
print()

for item in test_dict.items():
    print(item, end=' ')
print()

for key, value in test_dict.items():
    print(f'{key}: {value}')
print()


# плохо
if 'a' in test_dict:
    print(test_dict['a'])
else:
    print('нет ключа')

# хорошо
print(test_dict.get('a', 'нет ключа'))

