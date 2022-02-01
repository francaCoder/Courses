"""
Create a program that has a function called factorial() that will receive two parameters.
- The first: number
- the second: show.
if show = true the factorial'shortcut process will be showed else no

"""
from time import sleep


def factorial(n, show=False):
    if show:
        print("You chose see the process: ", end="")
        sleep(1)
        f = 1
        for c in range(n, 0, -1):
            f *= c
            print(f"{c}", end="")
            sleep(0.5)
            print(" x " if c > 1 else " → ", end="")
        print(f)
    else:
        print("The result is → ", end="")
        f = 1
        for c in range(n, 0, -1):
            # If show....
            f *= c
        print(f)


factorial(5, show=True)
