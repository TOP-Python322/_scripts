text = 'Python — самый крутой язык!'

print(type(text))
print(type(text[0]), end='\n\n')

# приведёт к TypeError
# text[0] = 'p'

for i in range(len(text)):
    print(str(i).rjust(3), end=' ')
print()

for char in text:
    print(char.rjust(3), end=' ')
print()

for i in range(-len(text), 0):
    print(str(i).rjust(3), end=' ')
print('\n')


text_ed = 'p' + text[1:]
print(text_ed, end='\n\n')
# >>> text[1:20]
# 'ython — самый круто'
# >>> text[1:40]
# 'ython — самый крутой язык!'
# >>>
# >>> text[40]
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# >>>
# >>> text[1:]
# 'ython — самый крутой язык!'
# >>>
# >>> text[:14]
# 'Python — самый'
# >>>
# >>> text[:]
# 'Python — самый крутой язык!'
# >>>
# >>> text[1:14:2]
# 'yhn—смй'
# >>>
# >>> text[20:14:-1]
# 'йотурк'
# >>>
# >>> text[::-1]
# '!кызя йотурк йымас — nohtyP'


text_listed = list(text)
print(text_listed, end='\n\n')

words = text.split()
print(words, end='\n\n')

parts = tuple(text.split(' — '))
print(parts, end='\n\n')
