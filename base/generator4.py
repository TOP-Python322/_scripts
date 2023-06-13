def doubled_range(start: int, stop: int, step: int = 1) -> int:
    for n in range(start, stop, step):
        yield n
        yield n


print(list(doubled_range(5, 10)))
print(list(doubled_range(0, -100, -6)))
