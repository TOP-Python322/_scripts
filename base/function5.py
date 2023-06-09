def test(pos1, pos2, /, pos_key, *, key1, key2):
    """Выводит переданные аргументы в stdout. Демонстрационная."""
    print(pos1, pos2, pos_key, key1, key2, end='\n\n')


test(1, 2, 3, key1=4, key2=5)
test(1, 2, key2=5, pos_key=3, key1=4)

# привдёт к TypeError
# test(1, 2, 3, 4, 5)

# привдёт к TypeError
# test(pos1=1, pos2=2, pos_key=3, key1=4, key2=5)



def write_musicfile_in_db(
        file: bytes,
        *,
        trackname: str,
        artist: str,
        albumname: str,
        filetype: str,
        samplerate: int,
        channels: int,
        bitdepth: int,
):
    """Записывает аудиофайл и его метаинформацию в соответствующие поля БД."""


file_obj = b'ffff'
# неудобно читается — непонятно, какой аргумент в какой параметр
# write_musicfile_in_db(
    # file_obj,
    # 'Boom',
    # 'Boomer',
    # 'BOOM',
    # 'MP3',
    # 44100,
    # 6,
    # 8
# )
write_musicfile_in_db(
    file_obj,
    trackname='Boom',
    artist='Boomer',
    albumname='BOOM',
    filetype='MP3',
    samplerate=44100,
    channels=6,
    bitdepth=8
)


def point_checker(x, y, /, arg1='h', arg2=False):
    """Проверяет точку на плоскости на соответствие чему-то там по какому-то там алгоритму."""


# неудобно читается — 
# point_checker(arg1='r', y=10, x=5)
# point_checker(arg2=True, x=3, y=2)

point_checker(5, 10, arg1='r')
point_checker(3, 2, arg2=True)

