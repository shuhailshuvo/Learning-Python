from datetime import datetime, date, time
from time import sleep

now = datetime.now()
print("Current Datetime", now)

today = date.today()
print("Current Date", today)
print("Current Day", today.day)
print("Current Month", today.month)
print("Current Year", today.year)

# difference between two dates
t1 = date(1971, 12, 16)
t2 = date(2020, 1, 8)
t3 = t2 - t1
print("t3 =", t3)

# String from datetime
dateString = now.strftime("%d/%m/%Y, %H:%M:%S")
print("date time string:", dateString)

# String to datetime
dateObj = datetime.strptime(dateString, "%d/%m/%Y, %H:%M:%S")
print("date time Obj:", dateObj)

print("Sleeping for 5 second")
sleep(5)
print("Print after 5 second")
# what's inside dateTime
# print(dir(datetime))
