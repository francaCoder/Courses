# Arrays
from array import array

# Int numbers, Float numbers and characters
numbers = array("i", [1, 2, 3, 4, 5, 6])
print(numbers)
print()
numbers.append(8)
print(numbers)
print()
numbers.insert(-1, 7)
print(numbers)
print()
numbers.pop(0)
print(numbers)
print()
del numbers[0]
print(numbers)
print()
numbers.remove(3)
print(numbers)