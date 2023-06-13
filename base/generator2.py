def counter(start: int) -> int:
    while start > 0:
        yield start
        start -= 1


for n in counter(5):
    print(n, end=' ')
print()


def infinite_counter(start: int = 0, step: int = 1) -> int:
    while True:
        yield start
        start += step

for letter, number in zip('abcdefghijklmnopqrstuvwxyz', infinite_counter()):
    print(letter, number, sep='=', end=' ')
print()


