def words_inverter(word1: str, word2: str):
    print('начало вызова функции')
    print(word1[::-1] + word2[::-2])


# >>> ret1 = words_inverter('aba', 'bab')
# начало вызова функции
# ababb
# >>> print(ret1)
# None
# >>> type(ret1)
# <class 'NoneType'>
# >>>
# >>> ret_pr = print()

# >>> print(ret_pr)
# None


def multiplier(numbers: list[float]) -> float:
    res = 1
    for n in numbers:
        res *= n
    return res


# >>> multiplier(range(2, 10))
# 362880


def div_rounder(number1: int | float, number2: int | float) -> float:
    return round(number1 / number2, 2)

