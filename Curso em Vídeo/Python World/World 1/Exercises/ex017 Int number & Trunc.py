# Make a code that read any real number and show just your whole portion
# Ex: number = 6.127    result = 6

from math import trunc

number = float(input("Type a real number: "))
print("The entered value was {} and your whole portion is {}.".format(number, trunc(number)))

# OR .format(number, int(number))
