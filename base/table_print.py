def table_print(*rows: list[int]):
    """Выводит в stdout переданные списки чисел в виде строк таблицы."""


def table_print(*columns: list[int]):
    """Выводит в stdout переданные списки чисел в виде столбцов таблицы."""


def table_print(table: list[list[int]]):
    """Выводит в stdout переданный список списков чисел в виде таблицы."""
    width = max(len(str(n)) for row in table for n in row)
    res = '\n'.join(
        ' '.join(
            str(n).rjust(width)
            for n in row
        )
        for row in table
    )
    print(res)


test_data = [
    [1, 100, -2],
    [23, 1, 254],
    [-15, 72, -132],
]
table_print(test_data)
