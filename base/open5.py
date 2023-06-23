words = [
    'дом',
    'яблоко',
    'слово',
    'человек',
    'дорога',
    'солнце',
]


with open('open5.txt', 'a', encoding='utf-8') as fileout:
    print(*words, file=fileout)
    print('', *words, sep='\n', end='\n23:28 22.06.2023', file=fileout)
