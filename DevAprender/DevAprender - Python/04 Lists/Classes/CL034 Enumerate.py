for number in range(0, 10):
    print(number)


# Enumerate - what's the current index

for index, number in enumerate(range(0, 10), 1):
    print(f"{index-1} → {number}")