from pathlib import Path


file_path = Path('open3.txt')


with open(file_path, 'w', encoding='utf-8') as fileout:
    fileout.write('тестовая запись для текстового файла')


with open(file_path, 'a', encoding='utf-8') as fileout:
    fileout.write('вторая\nболее длинаая\nтестовая запись для текстового файла')


