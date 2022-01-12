# Lists are mutable
# lists [] Tuples ()

n = (1, 2, 3, 4)
# n[2] = 3 ERROR
print(n)

num = [5, 6, 7, 8]
num[3] = 9
print(num)

# I can't add values to an index that doesn't exist
# I must use the append. Append = Push
num.append(10)
print(num)

# Ordered
num.sort()
print(num)

# Reverse
num.reverse()
print(num)

print(f"This list has {len(num)} elements.")

# Add an element in specific position
num.insert(2, 0) # Position 2 add number 0

# .pop = remove the last     .pop(2) remove the index 2
num.pop()
print(num)

num.pop(0)
print(num)

# del also removes
# .remove also removes
if 4 in num:
    num.remove(4)
else:
    print("I didn't find the 4")

values = []
values.append(5)
values.append(7)
values.append(9)


for counter in range(0, 5):
    values.append(int(input("Type a number")))

for index, number in enumerate(values):
    print(f"In the position {index}º i find the value {number}")
print("End")


a = [1, 2, 3]
b = [4, 5, 6]
b[2] = 8 # A also changes

