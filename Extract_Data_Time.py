import datetime
from sqlite3 import Time

now=datetime.datetime.now()
print(now)
Year=lambda x:x.year
Month=lambda x:x.month
day=lambda x:x.day
t=lambda x:x.time()

print(Year(now))
print(Month(now))
print(day(now))
print(t(now))