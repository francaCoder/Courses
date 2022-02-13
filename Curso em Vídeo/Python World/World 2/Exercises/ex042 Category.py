"""
Show the swim athlete's category according to age:
Until 9 Years - Little
Until 14 Years - Childish
Until 19 years - Junior
Until 20 years - Senior
above - Master
"""

age = int(input("What's your age? "))

if age <= 9:
    print("You're in category Little")
elif age <= 14:
    print("You're in category Childish")
elif age <= 19:
    print("You're in category Junior")
elif age <= 25:
    print("You're in category Senior")
else:
    print("You're in category Master")