"""
Make a code that will generate a 5 random numbers and put in a tuple.
After that, show the list of generated numbers and also show the higher and the smallest number.
"""

from random import randint

numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )

print("I drew the values {}".format(numbers))
print("The highest number drawn was {}".format(max(numbers)))
print("The smallest number drawn was {}".format(min(numbers)))