# Set - Remove equal values

numbers = [2, 2, 5, 8]
fruits = {"Apple", "Strawberry", "Lemon", "Apple", "Orange"}

set_numbers = set(numbers)
set_fruits = set(fruits)

print(set_numbers)
print(set_fruits)


# Join

numbers1 = [2, 2, 5, 8]
numbers2 = [2, 2, 3, 9]

a = set(numbers1)
b = set(numbers2)

# If I want to know the unique values in two arrays

print(a.symmetric_difference(b))

# Common values
print(a.intersection(b))

# unique values in two arrays
print(a.union(b))