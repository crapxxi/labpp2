import datetime

c = datetime.datetime.now()

x = datetime.datetime(c.year, c.month, c.day-5)

print(x)

print(datetime.datetime(c.year, c.month, c.day+1))
print(datetime.datetime(c.year, c.month, c.day-1))

print(c.strftime("%f"))

print((c-x).total_seconds())