"""
Make a code that read the year that the user was born and answer if
1 - It will still take time to enlist in army
2 - It's time to enlist
3 - The time to enlist has passed

The program also will must show the time is left or that has passed from enlistment
"""

from datetime import date

yearWasBorn = int(input("When you was born? "))
year = date.today().year
age = year - yearWasBorn
enlist = 18

if age < enlist:
    print("It will still take time to enlist in army. Present yourself from here {} years".format(enlist - age))
elif age == enlist:
    print("It's time to enlist.")
elif age > enlist:
    print("The time to enlist has passed {} years".format(age - enlist))
