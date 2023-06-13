from random import randrange as rr


def words_generator(amount: int) -> str:
    for _ in range(amount):
        word = ''.join(
            chr(rr(97, 123))
            for _ in range(rr(3, 10))
        )
        yield (word, word.capitalize())[rr(2)]


for word in words_generator(10**6):
    print(word, end=' ')
