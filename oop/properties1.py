from re import compile


class Book:
    pat_author = compile(r'[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+( [А-Я][а-я]+)?')

    def __init__(self, title: str, authors: list[str]):
        self.title = title
        # защищённый атрибут
        self.__authors = authors
    
    # геттер для атрибута __authors
    @property
    def authors(self) -> str:
        # доступ к защищёному атрибуту в локальных пространствах имён методов класса осуществляется без использования механизма подмены имён (name mangling)
        return self.__authors
    
    # сеттер для атрибута __authors
    @authors.setter
    def authors(self, new_authors: list[str]) -> None:
        for author in new_authors:
            if not self._pat_author.fullmatch(author):
                raise ValueError
        self.__authors = new_authors


besy = Book('Бесы', ['Фёдор Михайлович Достоевский'])

# вызов сеттера
# >>> besy.authors = 0.12
# ...
# TypeError: 'float' object is not iterable

# >>> besy.authors = [1, 2, 3]
# ...
# TypeError: expected string or bytes-like object, got 'int'

# >>> besy.authors = ['abc', '123']
# ...
# ValueError

# >>> besy.authors = ['Федор Достоевский']

# вызов геттера
# >>> besy.authors
# ['Федор Достоевский']