class Book:
    def __init__(self, title: str, authors: list[str]):
        # публичные атрибуты
        self.title = title
        self.authors = authors


catalog = [
    Book('Бесы', ['Фёдор Михайлович Достоевский']),
    Book('Наследники', ['Владислав Петрович Крапивин']),
    Book('Крылов', 123),
]

# >>> catalog[0].authors = 0.1
# >>>
# >>> for book in catalog:
# ...     print(book.authors)
# ...
# 0.1
# ['Владислав Петрович Крапивин']
# 123
# >>>
# >>> catalog[0].authors = ['1', '2', '3']
# >>>
# >>> for book in catalog:
# ...     print(book.authors)
# ...
# ['1', '2', '3']
# ['Владислав Петрович Крапивин']
# 123


from re import fullmatch


class Book:
    def __init__(self, title: str, authors: list[str]):
        # частный атрибут
        self._title = title
        # защищённый атрибут
        self.__authors = authors
    
    # геттер
    def title(self) -> str:
        return self._title
    
    # сеттер
    def title_setter(self, new_title: str) -> None:
        try:
            if fullmatch(r'[\w\.,:!?-]+', new_title):
                self._title = new_title
            else:
                raise ValueError('use only letters, digits and punctuation for title')
        except TypeError:
            raise ValueError('use only letters, digits and punctuation for title')


besy = Book('Бесы', ['Фёдор Михайлович Достоевский'])

# >>> besy._title = 123
# >>> besy._title
# 123

# >>> besy.__authors
# ...
# AttributeError: 'Book' object has no attribute '__authors'
# >>> 
# >>> besy.__dict__
# {'_title': 'Бесы', '_Book__authors': ['Фёдор Михайлович Достоевский']}

# использование механизма подмены имён (name mangling) при доступе из внешних (относительно объекта класса) пространств имён
# >>> besy._Book__authors = 123
# >>> besy.__dict__
# {'_title': 'Бесы', '_Book__authors': 123}



