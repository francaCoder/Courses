"""
it Looks like for, but the for we use when we know the beginning and the end
"""

for c in range(1, 5):
    print(c)
print("End")
print(" ")

c = 1
while c < 5:
    print(c)
    c += 1
print("End")
print(" ")

for c in range(1, 4):
    n = int(input("Type a value: "))
print("End")
print(" ")

n = 1
while n != 0:
    n = int(input("Type a value: "))
print("End")
print(" ")

r = "Y"
while r == "Y":
    n = int(input("Type a value: "))
    r = str(input("Do you want continue? [Y/N] ")).upper()
print("End")
print(" ")

n = 1
even = odd = 0
while n != 0:
    n = int(input("Type a value: "))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

print("You typed {} Even numbers and {} Odd numbers.".format(even, odd))
print("End")
print(" ")