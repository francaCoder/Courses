"""
Make a code that show a times table of several numbers for each number typed by user.
The program will be interrupted when the number is 999
"""

yes = "Y"
while yes == "Y":
    number = int(input("Choice a number to see the times table: "))
    if number == 999:
        break
    else:
        counter = 0
        print("{} x {} = {}".format(number, counter, number * counter))
        counter += 1