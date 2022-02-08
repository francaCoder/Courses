"""
Show index number + fruit's name. But when the index == 3, print:
"index + fruit's name + " at discount."
"""

fruits = ["Apple", "Orange", "Strawberry", "Lemon"]

for index, fruit in enumerate(range(0, len(fruits), 1)):
    if index == 3:
        print(f"{index} → {fruits[fruit]} at discount!!")
    else:
        print(f"{index} → {fruits[fruit]}")
