# Make a code that read the length of base and height and show the length of Hypotenuse.

from math import hypot

vertical = float(input("Height: "))
horizontal = float(input("Base: "))
hy = hypot(vertical, horizontal)

print("The hypotenuse will measure {:.2f}".format(hy))





