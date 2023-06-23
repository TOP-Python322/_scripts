from pathlib import Path
from pprint import pprint
from sys import path


print(Path.cwd(), end='\n\n')

pprint(path)

script_dir = Path(path[0])
gitignore_path = script_dir / '../.gitignore'
existence = "существует" if gitignore_path.is_file() else "не существует"
print(f'\n{gitignore_path!r} ({existence})\n')


text = gitignore_path.read_text(encoding='utf-8')
print(f'{type(text)}\n{text!r}')

text = (script_dir / '../git.txt').read_text(encoding='utf-8')
print(f'\n(utf-8) {text[:70]!r}')

text = (script_dir / '../git.txt').read_text(encoding='866')
print(f'\n(oem 866) {text[:70]!r}')

