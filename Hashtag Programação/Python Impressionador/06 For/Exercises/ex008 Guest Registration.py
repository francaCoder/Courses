"""
Create a system that records the arrival of guests at the hostel.
1 - Check how many persons per room
2 - According to number above, make a for asking the Name and CPF for each person
3 - Return a list with all informations
"""

how_many_persons = int(input("How many persons: "))

full_list = []

for c in range(how_many_persons):
    full_list.append([str(input("Name: ")), int(input("CPF: "))])

print(full_list)
