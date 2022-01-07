"""
Make a code that read a several whole numbers and then show the average between these and also the higher and smallest number.
The code must ask: "Do you want continue typing new values?"
"""

yes = "Y"
sum = 0
length = 0
average = 0
while yes == "Y":
    want = str(input("Do you want continue typing new values? [Y/N] ")).strip().upper()
    if want == "Y":
        number = int(input("Type a number: "))
        sum = sum + number
        length = length + (number / number)
        average = sum / length
    elif want == "N":
        print(" ")
        print("→ The sum between this numbers is {}".format(sum))
        print("→ You typed {:.0f} numbers".format(length))
        print("→ The average between this numbers is {:.1f}".format(average))
        print(" ")