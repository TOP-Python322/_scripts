def adder(number1, number2):
    print('\n\tначало вызова функции')
    print(f'\t{number1=} {number2=}')
    print(f'\t{number1 + number2}')



print('начало')

print(type(adder), adder, adder.__name__, sep='\n', end='\n\n')

adder(11, 9)
adder(5, 20)

adder(number1=24, number2=-10)
adder(number2=3, number1=27)

adder(8, number2=16)

# приводит к TypeError
# adder(1)
# adder()
# adder(1, 2, 3)
