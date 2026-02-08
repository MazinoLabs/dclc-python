from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Exercise 1
date = datetime.now()
print(date)


# Exercise 2
date_string = "Feb 25 2020 4:20PM"

a_date = datetime.strptime(date_string, '%b %d %Y %H:%M%p')
print(a_date)


# Exercise 3
a_week = timedelta(weeks=1)
given_date = datetime(2020, 2, 25)
prev_week = given_date - a_week
print(prev_week)


# Exercise 4
given_date = datetime(2020, 2, 25)
new_format = given_date.strftime('%A %d %B %Y')

print(new_format)


# Exercise 5
given_date = datetime(2020, 7, 26)
print(given_date.strftime('%A'))


# Exercise 6
given_date = datetime(2020, 3, 22, 10, 0, 0)
one_week = timedelta(weeks=1, hours=12)
print(given_date + one_week)


# Exercise 7
now = datetime.now()
milliseconds = int(now.timestamp() * 1000)
print(milliseconds)


# Exercise 8
given_date = datetime(2020, 2, 25)
str_date = given_date.strftime('%Y-%m-%d %H:%M:%S')
print(str_date)


# Exercise 9
given_date = datetime(2020, 2, 25).date()
four_months = relativedelta(month=4)
print(given_date+four_months)


# Exercise 10
date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)
print(f"{(date_2 - date_1).days} days")
