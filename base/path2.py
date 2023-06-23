from pathlib import Path

DIR_PATH = Path(r'd:\G-Doc\YandexDisk\Job\TOP Academy\Python web\322')

# >>> DIR_PATH
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/322')
# >>>
# >>> DIR_PATH / 'scripts'
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/322/scripts')
# >>>
# >>> DIR_PATH / r'..\321\scripts'
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/322/../321/scripts')
# >>>
# >>> DIR_PATH / '..' / '321' / 'scripts'
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/322/../321/scripts')
# >>>
# >>> DIR_PATH / '../321/scripts'
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/322/../321/scripts')
# >>>
# >>> (DIR_PATH / r'..\321\scripts').is_dir()
# True

# >>> scripts = DIR_PATH / 'scripts'
# >>> scripts.name
# 'scripts'
# >>> scripts.is_file()
# False
# >>> scripts.is_dir()
# True

# >>> Path(r'b:\file.txt')
# WindowsPath('b:/file.txt')
# >>>
# >>> Path(r'b:\file.txt').exists()
# False

