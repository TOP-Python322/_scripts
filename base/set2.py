mammals = {'тигр', 'верблюд', 'баран', 'кит', 'морж'}
aquatic = {'осьминог', 'креветка', 'краб', 'кит', 'морж'}

print(f'{mammals | aquatic = }')
print(f'{mammals & aquatic = }')
print(f'{mammals - aquatic = }')
print(f'{aquatic - mammals = }')
print(f'{aquatic ^ mammals = }\n')

aquatic_mammals = mammals & aquatic

print(f'{aquatic_mammals <= mammals = }\n')

reptiles = set()
for _ in range(4):
    reptiles.add(input('рептилия: '))
print(f'\n{mammals.isdisjoint(reptiles) = }')

