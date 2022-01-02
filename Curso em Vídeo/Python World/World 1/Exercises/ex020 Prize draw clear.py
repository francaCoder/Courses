# A teacher have draw somebody to clear the board.
# Make a code that read the name of students and choose one randomly

from random import choice

n1 = str(input("First name: "))
n2 = str(input("Second name: "))
n3 = str(input("Third name: "))
n4 = str(input("Fourth name: "))

nameList = [n1, n2, n3, n4]

print("The name chosen was {}".format(choice(nameList)))