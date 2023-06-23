from pathlib import Path


file_path = Path('_poker.py')


with open(file_path, encoding='utf-8') as filein:
    code_lines = filein.readlines()


code_lines = [
    line
    for line in code_lines
    if not line.lstrip().startswith('#')
]

with open('open4.txt', 'w', encoding='utf-8') as fileout:
    fileout.writelines(code_lines)
