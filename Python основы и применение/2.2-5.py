import datetime

year, month, day = input().split()
date = datetime.date(int(year), int(month), int(day))
days = datetime.timedelta(int(input()))

delta = date + days
print(delta.year, delta.month, delta.day)
