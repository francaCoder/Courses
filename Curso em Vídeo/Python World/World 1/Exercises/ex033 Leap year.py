# Make a code that read a number and show if it is a 'Leap year'

from datetime import date
# 0 = Current year
year = int(input("Type a year: "))

if year == 0:
    year = date.today().year
if year % 4 and year % 100 != 0 or year % 400 == 0:
    print("The year {} is a Leap year".format(year))
else:
    print("The year {} isn't a Leap year".format(year))