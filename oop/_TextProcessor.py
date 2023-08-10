from pathlib import Path
from string import ascii_letters, digits, whitespace
from sys import path


# переменные для аннотации
pathlike = str | Path


class TextProcessor:
    script_dir = Path(path[0])
    
    def __init__(self, text_file: pathlike, encoding: str = 'utf-8'):
        self.path = Path(text_file)
        self.text = self.path.read_text(encoding)
        # можно добавить атрибут экземпляра cleared_words
    
    def __repr__(self):
        return f"<'{self.path!s}': {len(self.cleared_words())} words>"
    
    # можно кешировать метод
    def cleared_words(self) -> list[str]:
        punctuation = set(self.text) - set(ascii_letters) - set(digits) - set(whitespace)
        return [
            word.strip(''.join(punctuation)).lower()
            for word in self.text.split()
        ]
    
    def unique_words(self) -> set[str]:
        return set(self.cleared_words())
    
    def rate_words(self) -> dict[str, int]:
        return {
            # неоптимальное использование метода cleared_words() — метод вызывается и вычисляется для каждой итерации 
            word: self.cleared_words().count(word)
            for word in self.unique_words()
        }


article = TextProcessor(r'd:\G-Doc\TOP Academy\Python web\322\scripts\oop\_text_eng.txt')

for word, rate in article.rate_words().items():
    print(f'{word!r}: {rate}')



