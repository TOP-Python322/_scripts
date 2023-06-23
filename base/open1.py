filein = open('_poker.py', encoding='utf-8')
text = filein.read()
filein.close()

print(type(filein))
print(f'\ntext = {text[:70]!r}')

