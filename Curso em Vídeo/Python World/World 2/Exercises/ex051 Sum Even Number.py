"""
Make a code that read 6 whole numbers and show the sum only of even numbers
if the number is odd disregard it
"""

sum = 0
for c in range(0, 6):
    numbers = int(input("Type a Whole Number: "))
    if numbers % 2 == 0:
        sum += numbers

print("The sum between these numbers is {}.".format(sum))
