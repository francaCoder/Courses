# How to create a list?

# Loops & range
numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)

# Map
names = ["Matheus", "Laryssa", "Rafael", "Marcos"]
def approve_person(name):
    return f"{name} approved."


print(list(map(approve_person, names)))


# List compreheension

new_list = [2 * i for i in range(10)]
print(new_list)


names = ["Matheus", "Laryssa", "Rafael", "Marcos"]
result = [name + " APPROVED" for name in names]
print(result)

print([approve_person(name) for name in names])


# Excel table
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

from pprint import pprint
from random import randint
pprint([[i for i in range(1, 6)] for x in range(5)])

print([approve_person(name) for name in names if name == "Matheus"])

print([i for i in range(20) if i not in (1, 5, 15, 19)])


def is_even_number(number):
    value = number % 2
    if value == 0:
        return True
    else:
        return False


print([i for i in range(20) if is_even_number(i)])


#

participants = ["Matheus", "Laryssa", "Rafael", "Marcos"]
winners = ["Matheus", "Marcos"]
print([i + " Winner" if i in winners else i + " Not selected" for i in participants])