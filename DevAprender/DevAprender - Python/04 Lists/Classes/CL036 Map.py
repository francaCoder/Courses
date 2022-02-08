# Creating lists

numbers = []
for n in range(5):
    numbers.append(n)
print(numbers)

# Map

names = ["Matheus", "Laryssa", "Rafael", "Gustavo"]


def approve_person(name):
    return f"{name}: Approved "


print(list(map(approve_person, names)))

# Map - will sweep the array, adding the return of function
# Map return True or False