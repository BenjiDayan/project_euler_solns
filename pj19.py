#pj19

import datetime

comp = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        temp = datetime.date(year, month, 1)
        if temp.weekday() == 6:
            comp += 1

print(comp)
