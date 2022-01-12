"""
Tuples - Ordered sequence of 'x' elements
Tuples ar immutable
() = Tuples
[] = List
{} = Dictionary
"""

snack = ("Hamburger", "Juice", "Pizza", "Pudding")
print(snack)
# How many index has the snack?
print(len(snack))
# We can show each element putting the index
print(snack[1]) # Hamburger
# We can show each element putting -index. (Beginning from right)
print(snack[-1]) # Pudding
# Show starting from element 1 to element 3
# The last element (number 3) is disregarded
print(snack[1:3]) # Juice and Pizza
# Element 2 to the End
print(snack[2:]) # Pizza and Pudding
# From the beginning to element 2
print(snack[:2]) # Hamburger, Juice, Pizza
# Starting from pizza and go to the beginning
print(snack[-2:])
# Sorted / Ordered
print(sorted(snack))


print(" ")
for food in snack:
    print(f"I'm going to eat {food}")
print("I ate too much ☻")
print(" ")

for counter in range(0, len(snack)):
    print(f"I'm going to eat {snack[counter]}")
print(" ")

for counter in range(0, len(snack)):
    print(f"I'm going to eat {snack[counter]} in the position {counter}")
print(" ")

for position, food in enumerate(snack):
    print(f"I'm going to eat {food} in the position {position}.")
print(" ")



a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
# a + b = 1, 2, 3, 4, 5, 6
# b + a = 4, 5, 6, 1, 2, 3
print(c)
# How many times the number 5 appear in → c
print(c.count(5))
# Which the index of number 4?
print(c.index(4))

exemple = (2, 0, 0, 0, 2, 0)
# Which the index of number 2 jumping the first
print(exemple.index(2, 1))


# I can put several elements of different types
person = ("França", 18, "M", 84)

# I can delete a tuples