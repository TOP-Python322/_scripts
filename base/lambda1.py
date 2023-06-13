# прямое присваивание lambda выражений в переменные крайне не рекомендуется
anonim_func = lambda: 'возвращаемое значение'
anonim_func2 = lambda: 'возвращаемое значение2'

print(f'{type(anonim_func)}\n{anonim_func}\n{anonim_func2}\n')

print(anonim_func())
print(anonim_func2())

print((lambda x, y: round(x / y, 2))(7, 2))

