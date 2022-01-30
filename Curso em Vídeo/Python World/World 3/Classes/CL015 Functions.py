"""
Functions are represented by → def.
Serves to simplify our life, we don't need to do the same things oftentimes.
"""

print("-"*30) # Line
print("   1º Exemple   ")
print("-"*30)

# After make the function, we need to call/run the function when we want to use
# And leave 2 empty lines above and below


def line():
    print("-"*30)


line()
print("   2º Exemple   ")
line()


# We can use parameters inside the parentheses
def block(msg): # msg = message
    print("-"*30)
    print(msg)
    print("-"*30)


block("   3º Exemple   ")
block("   4º Exemple   ")


# Exemple exercise

# a = 1
# b = 2
# s = a + b
# print(s)
#
# a = 3
# b = 4
# s = a + b
# print(s)
# .....


# If I put → calculate(4, 5) the program will give error because calculate() still don't exist
# But I can create

def calculate(a, b):
    s = a + b
    print(s)


calculate(1, 2) # 1, 2 = Arguments
calculate(10, 20) # 10, 20 = arguments


# I can also determine the arguments

calculate(a=8, b=6)
# Or
calculate(b=7, a=5)


# Also exist the packing (empacotamento), where the function will receive a several arguments.

def counter(* numbers):
    print(numbers)


counter(1, 2, 3)
counter(4, 5)
counter(6, 7, 8, 9)

# Were created tuples. Then I can do the same things of tuples


def newCounter(* numbers):
    for number in numbers:
        print(f"{number}, ", end="")
    if len(numbers) > 1:
        print(f"You typed → {len(numbers)} numbers.")
        print("Finish")
    else:
        print(f"You typed → {len(numbers)} number.")
        print("Finish")


newCounter(4)
newCounter(5, 6, 7, 8)


# We can work with lists also
# If I want to double the values of my list


def double(list):
    position = 0 # Starts from
    while position < len(list):
        list[position] *= 2
        position += 1


values = [1, 2, 3]
double(values)
print(values)








