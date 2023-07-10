from json import load, loads, dump, dumps
from pathlib import Path
from pprint import pprint


data_text = Path('stdlib6.json').read_text(encoding='utf-8')

# print(f'\ndata_text = {data_text}\n')

data = loads(data_text)

# print('data = ', end='')
# pprint(data)
# print()


data['biomaterials'] += ['pinetree', 'violet flower']

data_text = dumps(data, ensure_ascii=False, indent=2)

# print(f'\ndata_text = {data_text}\n')

Path('stdlib6_ed1.json').write_text(data_text, encoding='utf-8')

with open('stdlib6_ed1.json', encoding='utf-8') as filein:
    data = load(filein)

data['passage'] += ['_p_large_boulders', '_p_small_boulders']

with open('stdlib6_ed2.json', 'w', encoding='utf-8') as fileout:
    dump(data, fileout, ensure_ascii=False)
