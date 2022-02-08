# Range = Generating a value

print(type(range(30)))
print()

for number in range(5):
    print(number)

print()

for number in range(0, 10, 2): # Jumping 2 by 2
    print(number)

# Create list

numbers = []

for number in range(0, 201, 10):
    numbers.append(number)

print(numbers)

# OR

numbers = list(range(0, 201, 10))
print(numbers)