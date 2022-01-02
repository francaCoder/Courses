"""
The same teacher want draw the presentation order.
Make a code that read the name of 4 students and show the order drawn
"""

from random import shuffle

n1 = str(input("First name: "))
n2 = str(input("Second name: "))
n3 = str(input("Third name: "))
n4 = str(input("Fourth name: "))

orderedList = [n1, n2, n3, n4]
shuffle(orderedList)

print("The order will be:")
print(orderedList)