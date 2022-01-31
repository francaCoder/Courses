"""
Interactive help
Docstrings
Optional Arguments
Scope
Returns
"""

# Interactive help
# I can put help() in Python console and then any function, library, etc.
# Or here, help(function, library, etc.)
# Or print(input__doc__)
# Or press Ctr + click in anything


# Docstrings
# If someone uses or reads my function, they can't know how it works.
# Because we need use docstrings  """ ... """
# If we use the docstrings, we can use the help(Function's name)
def counter(beginning, end, jump):
    """
    => Do a counting and show on screen
    :param beginning: Starting number
    :param end: Final number
    :param jump: Jumping by
    :return: No return
    """
    loop = beginning
    while loop <= end:
        print(f"{loop}", end="..")
        loop += jump
    print("Finish")


counter(0, 100, 10)
help(counter)


# Optional arguments
# We have already seen Optional parameters using *
# If I can sum 2 or three numbers:
def sum(a=0, b=0, c=0):
    """

    :param a: Number
    :param b: Number
    :param c: Number
    :return: No return
    """
    s = a + b + c
    print(f"The sum between numbers was {s}")


# If I run sum() and passing just two arguments, will happen an error, because the functions has 3 parameters.
# To solve this, we will do "c" to receive 0
# And we can also make each parameter optional
sum(1, 2)


# Scope

def test(): # Local
    x = 10
    print(f"n → {n}")
    print(f"x → {x}")


# Global
n = 2
print(f"Main program: n = {n}")
test()
# print(x) # x is not defined

# The local scope has access to global scope
# But
# The global scope don't have access to local scope

# We can also create "equal variables", one in and one out function.(global and local scope)

n1 = 2


def myFunction():
    n1 = 1
    print(f"N1 in local scope→ {n1}")


myFunction()
print(f"N1 in global scope → {n1}")

# Or I can put:
# def myFunction():
#     global n1 # Reference
#     n1 = 1
#     print(f"N1 in local scope is 1 and in global scope is 1 too.")


# Return


def sum(a=0, b=0, c=0):
    s = a + b + c
    return s


result1 = sum(1, 2, 3)
result2 = sum(4, 5)
result3 = sum(6)
print(f"My calculations were {result1}, {result2} and {result3}")


# Exemple exercises -----------------------------


def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


number = int(input("Type a number: "))
print(f"The number's factorial is {factorial(number)}")

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f"The results are {f1}, {f2} and {f3}")


def evenNumber(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


number = int(input("Type a number: "))
print(evenNumber(number))