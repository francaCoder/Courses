"""
Make a code that read the name, age and gender. In the end show:
- The group's average age
- Who is the old man
_ How many women has lass than 20 years
"""


totalAge = 0
gender = 0
biggestAgeMan = 0
oldMan = ""
totalWomen = 0
for person in range(1, 5):
    print("------ {}ª People ------ ".format(person))
    name = str(input("Name: "))
    age = int(input("Age: "))
    gender = str(input("[M/F]: ")).strip()
    totalAge += age
    if person == 1 and gender in "Mm":
        biggestAgeMan = age
        oldMan = name
    if gender in "Mm" and age > biggestAgeMan:
        biggestAgeMan = age
        oldMan = name
    if gender in "Ff" and age < 20:
        totalWomen += 1

averageAge = totalAge / 4
print("The average age's groups is {} years.".format(averageAge))
print("The old man has {} years and called {}.".format(biggestAgeMan, oldMan))
print("Altogether are {} women with under twenty years.".format(totalWomen))


