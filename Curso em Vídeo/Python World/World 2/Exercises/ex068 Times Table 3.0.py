"""
Make a code that show a times table of several numbers for each number typed by user.
The program will be interrupted when the number is negative
"""

from time import sleep

while True:
    number = int(input("Do you want see the times table of which number? "))
    while number == 0:
        number = int(input("Do you want see the times table of which number? "))
    if number > 0:
        print("↓ ↓ ↓ ↓ ↓ Finish ↓ ↓ ↓ ↓ ↓")
        for c in range(1, 11):
            print("{} x {} = {}".format(number, c, number * c))
        print("↑ ↑ ↑ ↑ ↑ Finish ↑ ↑ ↑ ↑ ↑")
    if number < 0:
        print("Program closed, always come back. ")
        break