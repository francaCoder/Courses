"""
Logical operators
Boolean operators
Equality operators
"""

age = 15
print(age > 21) # False
print(age < 21)
print(age >= 21)
print(age <= 21)
print(age == 21)
print(age != 21)

print(True == True)
print("Matheus" == "matheus")
print("b" > "a")
print(5 == "5")


age = 21
has_an_invitation = False
owners_son = True
if (age >= 21 and has_an_invitation == True) or (owners_son == True):
    print("Free access")
else:
    print("Access denied")

# And = 2 requirements
# Or = 1 requirement


print("--- Hiring ---")
# we want to hire people that still haven't own car but already has a work card
over_age = True
work_card = True
currently_working = False
own_car = False

if over_age == True and currently_working == False:
    if work_card == True and not own_car:
        print("Hired")