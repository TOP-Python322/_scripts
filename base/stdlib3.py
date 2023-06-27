from datetime import date
from datetime import datetime as dt
from datetime import time
from datetime import timedelta as td


# >>> date(2020, 12, 31)
# datetime.date(2020, 12, 31)
# >>>
# >>> date.today()
# datetime.date(2023, 6, 27)
# >>>
# >>> dt.now()
# datetime.datetime(2023, 6, 27, 22, 59, 39, 351720)
# >>> dt.now().date()
# datetime.date(2023, 6, 27)
# >>>
# >>> date.fromtimestamp(165489786)
# datetime.date(1975, 3, 31)
# >>>
# >>> date.fromtimestamp(16548978600)
# datetime.date(2494, 6, 1)


# >>> date.fromtimestamp(1)
# datetime.date(1970, 1, 1)
# >>>
# >>>
# >>> today = date.today()
# >>> today.year
# 2023
# >>> today.month
# 6
# >>> today.day
# 27
# >>>
# >>> today - date(2020, 12, 31)
# datetime.timedelta(days=908)
# >>>
# >>> today.weekday()
# 1
# >>> today.isoweekday()
# 2
# >>> str(today)
# '2023-06-27'
# >>>
# >>> f'{today:%d.%m.%y}'
# '27.06.23'
# >>>
# >>> f'{today:%d/%m/%y}'
# '27/06/23'
# >>>
# >>> f'{today:%d - %m %y}'
# '27 - 06 23'
# >>>
# >>> f'{today:%d %B %y}'
# '27 June 23'
# >>>
# >>>
# >>> dt.strptime('01.01.2000', '%d.%m.%Y')
# datetime.datetime(2000, 1, 1, 0, 0)
# >>>
# >>> dt.now().timestamp()
# 1687889069.719092


# >>> dt1 = dt.now()
# >>> dt2 = dt.now()
# >>>
# >>> dt2 - dt1
# datetime.timedelta(seconds=16, microseconds=863656)
# >>>
# >>> td1 = dt2 - dt1
# >>> td1.seconds
# 16
# >>>
# >>> td1 = dt2 - dt.strptime('01.01.2000', '%d.%m.%Y')
# >>> td1.seconds
# 83812
# >>>
# >>> td1.days
# 8578
# >>>
# >>> td(hours=30)
# datetime.timedelta(days=1, seconds=21600)
# >>>
# >>> td(hours=30) * 2
# datetime.timedelta(days=2, seconds=43200)
# >>>
# >>> dt.now() + td(hours=30)
# datetime.datetime(2023, 6, 29, 5, 21, 32, 750236)
# >>>
# >>> 24 * 60 * 60
# 86400
# >>>
# >>> td(hours=30).seconds
# 21600
# >>>
# >>> td(hours=30).days*24*3600 + td(hours=30).seconds
# 108000
