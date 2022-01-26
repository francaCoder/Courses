"""
Lists within lists
"""

test = []

test.append("Gustavo")
test.append(40)
print(test) # [...]

peoples = []
peoples.append(test)
print(peoples) # [[....]]

"""
When i written .append(test), i added the original array, doing the link.
If i change any index of test, will change in peoples too
"""

newTest = []
newTest.append("Gustavo")
newTest.append(40)

newPeoples = []
newPeoples.append(newTest[:]) # [:] Copy
newTest[0] = "Maria"
newTest[1] = 22
newPeoples.append(newTest[:]) # [:] Copy
print(newPeoples)

# Or at the beginning:

guys = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(guys) # All...
print(guys[0]) # ["João", 19]
print(guys[0][0]) # João

for people in guys:
    print(people)
    # print(people[0]) → Just the name
    # print(f"{people0} has {people[1]} years old")

print(" ")

newGuys = []
data = []
overAge = underAge = 0

for c in range(0, 3): # How many peoples
    data.append(str(input("Name: ")))
    data.append(int(input("Age: ")))
    newGuys.append(data[:])
    data.clear()

# print(newGuys)

for people in newGuys:
    if people[1] >= 21:
        print(f"{people[0]} is over age")
        overAge += 1
    else:
        print(f"{people[0]} is under age")
        underAge += 1

print(f"We have {overAge} over age and {underAge} under age.")