"""
Make a code that read the name, age and gender. In the end show:
- The group's average age
- Who is the old man
_ How many women has lass than 20 years
"""


# totalAge = 0
# gender = 0
# biggestAgeMan = 0
# oldMan = ""
# totalWomen = 0
# for person in range(1, 5):
#     print("------ {}ª People ------ ".format(person))
#     name = str(input("Name: "))
#     age = int(input("Age: "))
#     gender = str(input("[M/F]: ")).strip()
#     totalAge += age
#     if person == 1 and gender in "Mm":
#         biggestAgeMan = age
#         oldMan = name
#     if gender in "Mm" and age > biggestAgeMan:
#         biggestAgeMan = age
#         oldMan = name
#     if gender in "Ff" and age < 20:
#         totalWomen += 1
#
# averageAge = totalAge / 4
# print("The average age's groups is {} years.".format(averageAge))
# print("The old man has {} years and called {}.".format(biggestAgeMan, oldMan))
# print("Altogether are {} women with under twenty years.".format(totalWomen))

# Or

people = []
men = []
oldMan = []
ages = []

totalWomen = average = 0

for c in range(0, 3):
    print(f"------ {c+1}ª People ------ ")
    person = {
        "Name": str(input("Name: ")),
        "Age": int(input("Age: ")),
        "Gender": str(input("Gender [M/F] ")).strip().upper()[0],
    }
    while person['Gender'] not in "MF":
        person['Gender'] = str(input("Gender [M/F] ")).strip().upper()[0]
    people.append(person)

    if person['Gender'] == "M":
        men.append([person['Name'], person['Age']])
        ages.append(person['Age'])

    if person['Gender'] == "F" and person['Age'] < 20:
        totalWomen += 1

for person in range(0, len(people)):
    average += people[person]['Age'] / len(people)

for man in men:
    if man[1] == max(ages):
        oldMan.append(man[0])


print("-=-=-=-= Result =-=-=-=-")
if len(oldMan) > 1:
    print("Os mais velhos são: ", end="")
    for old in oldMan:
        print(f"/ {old}", end="")
    print(f" com {max(ages)} anos")
elif len(oldMan) == 1:
    print(f"O mais velho é o {oldMan[0]} com {max(ages)} anos.")
else:
    print("Não existe homens no grupo.")

if totalWomen > 1:
    print(f"{totalWomen} mulheres do grupo tem menos do que 20 anos.")
elif totalWomen == 1:
    print(f"Apenas {totalWomen} mulher do grupo tem menos do que 20 anos.")
else:
    print("Não existem mulheres no grupo.")

print(f"A média de idade do grupo é de {average:.2f} anos")



