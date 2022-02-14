"""
# 1
Using the list compreheension, create the following list:
[2, 4, 6, 8, 10]

# 2
using the following list as a basis:
colors = ["Red", "Blue", "Green", "Yellow", "Pink", "Black"]

For create the list:
["1 - Red", "2 - Blue".....]


# 3
using the following lists as a basis:
participants = ["Joel", "Jéssica", "Maria", "Cris", "Laryssa", "Rafael", "Marcos", "Jhon"]
payment_made = ["Joel", "Jéssica", "Maria", "Cris"]

using conditions, concatenate the word "paid" to names from payment_made list
"""


# 1
print([2 * i for i in range(1, 6)])


# 2
colors = ["Red", "Blue", "Green", "Yellow", "Pink", "Black"]
c = 1
new_colors = []
for i in colors:
    new_colors.append(f"{c} - {i}")
    c += 1
print(new_colors)

# Or
colors = ["Red", "Blue", "Green", "Yellow", "Pink", "Black"]
# c = 1
# new_colors = [f"{c} - {color}" for color in colors]
# print(new_colors)
print([f"{str(colors.index(i)+1)} - {i}" for i in colors])

# 3
participants = ["Joel", "Jéssica", "Maria", "Cris", "Laryssa", "Rafael", "Marcos", "Jhon"]
payment_made = ["Joel", "Jéssica", "Maria", "Cris"]
print([f"{name} paid" for name in payment_made])
