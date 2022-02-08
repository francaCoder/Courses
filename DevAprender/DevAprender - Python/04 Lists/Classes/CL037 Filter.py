# Filter - Sweep an array

names = ["Matheus", "Marcos", "Murilo", "Miguel"]

# Marcus


def approve_person(name):
    if name == "Marcos":
        return True
    else:
        return False


print(list(filter(approve_person, names))) # Return the object/any information


paintings = [
    ["Classical Painting", "Blue", 1857],
    ["Medieval Painting", "Red", 1867],
    ["Modern Painting", "Green", 1897],
]


def antiquity(painting):
    if painting[2] < 1890:
        return True
    else:
        return False


print(list(filter(antiquity, paintings)))
print(list(map(antiquity, paintings)))