"""
Make a code that read two whole numbers and compare them, showing on the screen a message:
1 - The first value is biggest
2 - The second value is biggest
3 - Don't exist the biggest value, the two are equal
"""

n1 = int(input("First Number: "))
n2 = int(input("Second Number: "))

if n1 > n2:
    print("The first value is biggest.")
elif n2 > n1:
    print("The second value is biggest:")
else:
    print("This numbers have the same value.")