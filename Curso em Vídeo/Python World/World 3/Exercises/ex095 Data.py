"""
Create a program that read name, age and gender of several people, saving tha data of each person in a dictionary and all dictionaries in a list. And in the end, show:
- How many people were registered
- The average of age
- One list with all women
- One list with all people with age over the average
"""

guys = []
person = {}
sum = average = 0
# while True:
#     person.clear()
#     person['Name'] = str(input("Name: "))
#     while True:
#         person['Gender'] = str(input("Gender: [M/F] ")).strip().upper()[0]
#         if person['Gender'] in "MF":
#             break
#         print("[ERROR] Please, type just M to male or F to Female.")
#     person['Age'] = int(input("Age: "))
#     sum += person['Age']
#     guys.append(person.copy())
#     while True:
#         answer = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
#         if answer in "YN":
#             break
#         print("[ERROR] Please type just Y to Yes or N to No.")
#     if answer == "N":
#         break
while True:
    person.clear()
    person['Name'] = str(input("Name: "))
    person['Gender'] = str(input("Gender: [M/F] ")).strip().upper()[0]
    while person['Gender'] not in "MF":
        print("[ERROR] Please, type just M to male or F to Female.")
        person['Gender'] = str(input("Gender: [M/F] ")).strip().upper()[0]
    person['Age'] = int(input("Age: "))
    sum += person['Age']
    guys.append(person.copy())

    wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        print("[ERROR] Please type just Y to Yes or N to No.")
        wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    if wantContinue == "N":
        break
print("-="*30) # Data reading
print(f"Altogether we have {len(guys)} people registered.")
average = sum/len(guys)
print(f"The average of age is → {average:5.1f} years old.")
print(f"The women registereds were", end=" ")
for p in guys:
    if p['Gender'] == "F":
        print(f"{p['Name']} → ")
print()
print("People's list that who over age: ")
for p in guys:
    if p['Age'] > average:
        print("     ", end="")
        for k, v in p.items():
            print(f"{k} → {v}; ", end=" ")
        print()
print("<< Finished >>")

# Or

guys = []

while True:
    name = str(input("Name: "))
    gender = str(input("Gender: [M/F] ")).strip().upper()[0]
    while gender not in "MF":
        print("Type a valid gender [M/F]")
        gender = str(input("Gender [M/F] ")).strip().upper()[0]
    age = int(input("Age: "))
    while age <= 0:
        print("Type a valid age")
        age = int(input("Age: "))
    wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        print("Type Y to Yes or N to No")
        wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    print()
    person = dict()
    person['Name'] = name
    person['Gender'] = gender
    person['Age'] = age
    guys.append(person)
    if wantContinue == "N":
        break
print(guys)
print(f'The group has {len(guys)} people.')
sumAge = sumAverage = 0
for i in range(0, len(guys)):
    sumAge += guys[i]['Age']
    sumAverage = sumAge / (i + 1)
print(f"The average of age is {sumAverage} years.")
print(f"The women registereds were ", end="")
for i in range(0, len(guys)):
    if guys[i]['Gender'] == "F":
        print(f" → {guys[i]['Name']}", end=", ")
print()
print("People's list who are over age:")
for i in range(0, len(guys)):
    if guys[i]['Age'] > sumAverage:
        print(f"Name = {guys[i]['Name']}; Gender = {guys[i]['Gender']}; Age = {guys[i]['Age']};")
        print()


