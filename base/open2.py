from pathlib import Path
from pprint import pprint


file_path = Path('_poker.py')


with open(file_path, encoding='utf-8') as filein:
    text_lines = filein.readlines()

pprint(text_lines)
print('\n')


with open(file_path, encoding='utf-8') as filein:
    for line in filein:
        print(line.strip())



