from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from sys import modules


file_path = Path('1.py')
module_name = 'module111111'

spec = spec_from_file_location(module_name, file_path)
# создание объекта модуля
module1 = module_from_spec(spec)

modules[module_name] = module1

print('создание объекта модуля завершено')

spec.loader.exec_module(module1)

