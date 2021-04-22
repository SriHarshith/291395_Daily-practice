year = int(input("Enter year: "))
month = int(input("Enter month between 1 and 12: "))
date = int(input("Enter date between 1 and 31: "))

#checking for leap year
if year % 400 == 0:
    leap_year = True
elif year % 4 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
else:
    leap_year = False

#checking no. of days in month
if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month == 2:
    if leap_year:
        days = 29
    else:
        days = 28
else:
    days = 30

#calculating next date
if date < days:
    date += 1
else:
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is {}-{}-{}".format(date,month,year))
