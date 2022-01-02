# Make a code that read an angle and show your Sine => Cosine => Tangent

from math import sin, cos, tan, radians

angle = int(input("Put the angle: "))
s = sin(radians(angle))
c = cos(radians(angle))
t = tan(radians(angle))

print("The angle that you chosen was {}".format(angle))
print("Follow the informations:")
print("Sine: {:.2f}".format(s))
print("Cosine: {:.2f}".format(c))
print("Tangent: {:.2f}".format(t))