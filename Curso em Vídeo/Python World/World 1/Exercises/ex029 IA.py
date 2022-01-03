"""
Make a code that does the computer "think" in a whole number between 0 and 5, and ask
to user if he can answer what was the number chosen by computer
"""

from random import randint
from time import sleep

computer = randint(0, 5)   # Makes the computer think

number = int(input("I will think of a number between 0 and 5, try to guess: "))
print("Processing...")
sleep(1.5)

if number == computer:
    print("Congratulations, you defeated me! :(")
else:
    print("HAHAHA you missed, i thought in {} not in {}".format(computer, number))

# 4, 5, 2, 1, 3