import calendar

print(calendar.calendar(2026))

print(calendar.month(2026, 6))

day=calendar.weekday(2026, 6, 30)
print(day)

day=calendar.weekday(2026, 6, 30)
print(calendar.day_name[day])

print(list(calendar.month_name))
print(list(calendar.day_name))

#find the no of days
days= calendar.monthrange(2026 ,2)
print(days)

print(calendar.isleap(2024))

print(calendar.leapdays(2000, 2030))

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2026, 6))

cal=calendar.monthcalendar(2026 ,6)
print(cal)

year=int(input("enter year :"))

if calendar.isleap(year):
    print("leap year")
else:
    print("not a leap year ")
    
cal= calendar.Calendar()
for day in cal.itermonthdays(2026, 6):
    print(day)
    
cal= calendar.Calendar()
for d in cal.itermonthdates(2026, 6):
    print(d)
    
html_cal=calendar.HTMLCalendar()
print(html_cal.formatmonth(2026 ,6))

tc=calendar.TextCalendar()
print(tc.formatmonth(2026, 6, w=3 ,l=2))

import calendar
from datetime  import date
today= date.today()
print(calendar.day_name[today.weekday()])


from datetime import datetime
import time

while True:
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)