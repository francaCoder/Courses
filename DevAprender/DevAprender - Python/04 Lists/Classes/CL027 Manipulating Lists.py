values = list(range(1, 11))
years = list(range(2020, 2060, 10))

print(values)
print(years)

values.append(11) # Add at the end
print(values)

# join lists = Extend
print()

values.extend(years)
print(values)

years.insert(1, 2021)
print(years)

years.pop() # Remove the last element. Or can I pass the index of which element that will be removed
print(years)

# Or
del years[3] # Also remove
del years[1:]

years.count(2) # How many times appear the number 2

years.clear() # Deleting all items