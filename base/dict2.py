char_codes1 = { 
    char: code // 10
    for char, code in zip('abcdef', [12, 23, 49, 2, 57, 30])
}
char_codes2 = { 
    char: code // 10
    for char, code in zip('defghi', [98, 21, 82, 19, 20, 63])
}

print(char_codes1, id(char_codes1))
print(char_codes2, end='\n\n')

# создание новых объектов

# Python 3.9+
print(char_codes1 | char_codes2)
print(char_codes2 | char_codes1, end='\n\n')

char_codes1 = char_codes1 | char_codes2
print(char_codes1, id(char_codes1))


# изменение существующих объектов

# Python 3.9+
char_codes1 |= {'j': 2}
print(char_codes1, id(char_codes1))

# в любой версии
char_codes1.update({'k': 5})
print(char_codes1, id(char_codes1))

