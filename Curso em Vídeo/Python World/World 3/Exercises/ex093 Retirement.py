"""
Make a code that read the name, year of birth and the work card, and save them (With age) in a dictionary. If by chance the work card is different from 0, the work card also will receive the year of hired and the wage. You also must show with how many years this person will retirement.
"""

person = {}

person['Name'] = str(input("Name: "))
person['Age'] = 2021 - int(input("Was born in: "))
person['Work Card'] = int(input("Work Card: (0 = Don't have) "))
if person['Work Card'] != 0:
    person['Year of hired'] = int(input("Year of hired: "))
    person['Wage'] = float(input("Wage: "))
    person['Retirement'] = (person['Year of hired'] + 35) - (person['Age'] + 2021)


for key, value in person.items():
    print(f"{key} is → {value}")