from random import choices, randint

"""
Using the following list as a basis:
prize_draws = ["Prize draw1", "Prize draw2", "Prize draw3", ]
participants = ["Joel", "Jéssica", "Maria", "Cris", "Larissa", "Rafael", "Marcos", "Jhon"]

print on screen the winner of each prize draw. Selecting the winner using the library random.
exemple:
    {
        prize draw1: "Cris",
        prize draw2: "Rafael",
        prize draw3: "Marcos"
    }
"""

prize_draws = ["Prize draw1", "Prize draw2", "Prize draw3", ]
participants = ["Joel", "Jéssica", "Maria", "Cris", "Larissa", "Rafael", "Marcos", "Jhon"]
# result = {
#     prize_draws[0]: choices(participants)[0],
#     prize_draws[1]: choices(participants)[0],
#     prize_draws[2]: choices(participants)[0],
# }
# print(result)
for i in prize_draws:
    print({f"{i}": choices(participants)[0]})
# Or
print({prize_draw: choices(participants)[0] for prize_draw in prize_draws})

# 2

"""
We need data to create a temporary accounts, each group should receive an array with 5 random numbers (between 1 and 100)

groups = ["Group 1", "Group 2", "Group 3"]
result:
    {
        "Grupo 1": [93, 97, 63, 36, 64],
        "": [].....,
    }
"""

groups = ["Group 1", "Group 2", "Group 3"]
for group in groups:
    print({f"{group}": [randint(1, 100) for c in range(5)]})
# Or
print({group: [randint(1, 100) for i in range(5)] for group in groups})
