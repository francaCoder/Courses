# Show the factorial of a number choose by user

from math import factorial
n = int(input("Choice a number to calculate your factorial: "))
f = factorial(n)
print("The factorial of {} is {}".format(n, f))


# OR


from time import sleep

n = int(input("Choice a number to calculate your factorial: "))
c = n
f = 1
print("Calculating {}!".format(n), end=" ")
sleep(1)
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f)