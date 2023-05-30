test_set = {1, 2, 3, 4, 5, 2, 3}

print(test_set)

text = """update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two)"""

unique_chars = set(text)
print(unique_chars)
print(f'{len(text) = }')
print(f'{len(unique_chars) = }\n')


for char in unique_chars:
    print(char, end='')
print()

