from random import randrange as rr

# найти самую старшую комбинацию в руке
    # старшая карта
    # пара
    # две пары
    # сет
    # стрит
    # фулл-хаус
    # каре


hand = tuple(rr(2, 15) for _ in range(5))

unique = set(hand)
unique_len = len(unique)

result = 'старшая карта'

if unique_len == 5:
    # (4, 10, 3, 11, 9) -> [3, 4, 9, 10, 11] == [3, 4, 5, 6, 7]
    lowest = min(hand)
    if sorted(hand) == list(range(lowest, lowest+5)):
        result = 'стрит'

if unique_len == 4:
    result = 'пара'

repeats = max(hand.count(card) for card in unique)

if unique_len == 3:
    # (4, 10, 4, 11, 4) -> {4, 10, 11}
    if repeats == 3:
        result = 'сет'
    # (4, 10, 4, 11, 10) -> {4, 10, 11}
    elif repeats == 2:
        result == 'две пары'

if unique_len == 2:
    if repeats == 4:
        result = 'каре'
    elif repeats == 3:
        result == 'фулл-хаус'

print(hand)
print(result)
