# Read 3 numbers and show what's the biggest and what's the smallest

from time import sleep
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))

print("Precessing...")
sleep(2)


if n1 > n2 and n1 > n3:
    print(f"The biggest number is {n1}")
if n2 > n1 and n2 > n3:
    print(f"The biggest number is {n2}")
if n3 > n1 and n3 > n2:
    print(f"The biggest number is {n3}")

if n1 < n2 and n1 < n3:
    print(f"The smallest number is {n1}")
if n2 < n1 and n2 < n3:
    print(f"The smallest number is {n2}")
if n3 < n1 and n3 < n2:
    print(f"The smallest number is {n3}")
