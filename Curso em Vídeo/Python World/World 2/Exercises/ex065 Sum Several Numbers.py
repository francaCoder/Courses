"""
Make a code that read a several numbers and do the sum and show how many numbers was typed
between these. With 999 as stop condition. (Disregarding the flag)
"""

yes = "Y"
sum = 0
numbers = 0

while yes == "Y":
    number = float(input("Type a number: "))
    if number != 999:
        sum += number
        numbers = numbers + (number / number)
    else:
        yes = "N"
print(" ")
print("The sum between this numbers was {}".format(sum))
print("You typed {} numbers".format(numbers))

# OR

"""
num = 0
counter = 0
sum = 0
"""
num = counter = sum = 0
num = int(input("Type a number. (999 to stop) "))
while num != 999:
    sum += num
    counter += 1
    num = int(input("Type a number. (999 to stop) "))
print("You typed {} numbers and the sum between these was {}.".format(counter, sum))
# .format(counter - 1, sum - 999) or sum = sum - 999
