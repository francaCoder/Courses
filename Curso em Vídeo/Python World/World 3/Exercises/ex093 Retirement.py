"""
Make a code that read the name, year of birth and the work card, and save them (With age) in a dictionary. If by chance the work card is different from 0, the work card also will receive the year of hired and the wage. You also must show with how many years this person will retirement.
"""
from datetime import datetime

data = {}
data['Name'] = str(input("Name: "))
wasBornIn = int(input("Year of birth: ")) # 'Data' don't receive this
data['Age'] = datetime.now().year - wasBornIn # Current year
data['Work Card'] = int(input("Work Card: (0 = Don't Have) "))
if data['Work Card'] != 0:
    data['Year of hired'] = int(input("Year of hired: "))
    data['Wage'] = float(input("Wage: $"))
    # data['Retirement'] = data['Age'] + (data['Year of hired'] + 35) - datetime.now().year # Something to man and woman
    data['Retirement'] = (data['Year of hired'] - wasBornIn) + 35
for k, v in data.items():
    print(f"{k} → {v}")
print(data)

