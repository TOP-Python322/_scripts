from re import compile

date_pattern = compile(r'(?P<day>0[1-9]|[12]\d|3[01])'
                       r'(?P<sep>[\./\\-])'
                       r'(?P<month>0[1-9]|1[0-2])'
                       r'(?P=sep)'
                       r'(?P<year>\d{4})')

text = '''01.01.2000 — день начала третьего тысячелетия. Он не совпадет с началом так называемой "информационной эпохи" 01-01-1970.'''

all_dates = date_pattern.findall(text)
print(all_dates, end='\n\n')

all_dates = date_pattern.finditer(text)

for match_object in all_dates:
    print(match_object)
    print(match_object[0], end='\n\n')
