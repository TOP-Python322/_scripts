def test(**kwargs: float):
    print(f'\n{type(kwargs)}\n{kwargs}')


test(a=1, b=2, c='wow', switch=None)

params = {
    'kwarg1': 23,
    'kwarg2': 1.49,
    'kwarg3': 2**10,
    'kwarg4': ['mu']*5,
}
test(**params)



def fullhouse(pos, /, pos_key, *pos_args, key, **kwargs):
    pass


fullhouse(1, 2, key=3)
