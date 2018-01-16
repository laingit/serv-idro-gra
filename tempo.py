import calendar
import locale as lo

lo.setlocale(lo.LC_ALL, "")

c = calendar.TextCalendar()
c.prmonth(2014, 1)

for d in c.itermonthdays2(2014, 1):
    print(d)

