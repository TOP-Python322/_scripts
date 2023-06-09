def test(*args):
    print(f'\n{type(args)}\n{args}')


test()
test(1, 'abc')
test([10, 20, 30])
test(*[10, 20, 30])


def test2(arg1, *args: int):
    print(f'\n{arg1}, {args}')


# привдёт к TypeError
# test2()

test2(1)
test2(1, 2, 3)

test2(arg1=10)
# привдёт к TypeError
# test2(4, 5, arg1=10)


def test3(arg1='VAL', *args: str):
    print(f'\n{arg1}, {args}')


test3()
test3('a', 'b', 'c')


def test4(arg1, *args, kwarg):
    print(f'\n{arg1}, {args}, {kwarg=}')


# привдёт к TypeError
# test4(*range(1000))

test4(*range(20))
test4(*range(20), kwarg='\n')
