from typing import Literal


class Person:

    class Sex:
        def __init__(self, value: Literal['мужской', 'женский']):
            self.value = value

        def __repr__(self):
            return self.value

    def __init__(self, name: str, sex: Sex):
        self.name = name
        self.sex = sex

    def __repr__(self):
        return f'<{self.name}: {self.sex!r}>'

