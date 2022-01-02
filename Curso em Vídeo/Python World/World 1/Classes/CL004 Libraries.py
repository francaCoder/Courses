# The language python is simplem, but we can add new functionalities using the libraries.
# For exemple, we need add food and drinks in our body along the day
# Sometimes we need import new functionalities for create our program using:
# Import (name)

# If i want import specific things, i need reverse
# from (name) import (element)

# For exemple - import math
# Ceil - increase note
# Floor - decrease note
# Trunc - Delete numbers after comma
# pow - Potency
# sqrt - Square root
# Factorial - factorial numbers

# If i want use only sqrt
# From math import sqrt

# If i want two functionalities
# From math import sqrt, Floor

from math import sqrt, floor, ceil, trunc
number = int(input("Type a number: "))
root = sqrt(number)

print("Square root of {} is equal to {:.2f}".format(number, root))

# Find it out new libraries
# www.python.org -> Docs -> Version -> Libraries reference

import random
newNumber = random.random()
# Random 0 - 1
# Randint 1 - 10
print(newNumber)


import emoji
# Error -> Red lamp -> install   or    www.python.org -> PyPi
print(emoji.emojize("Hello, world :earth_americas:", use_aliases=True))



