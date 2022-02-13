"""
Make a code that read a several whole numbers and then show the average between these and also the higher and smallest number.
The code must ask: "Do you want continue typing new values?"
"""

yes = "Y"
sum = length = average = higher = smallest = 0
while yes == "Y":
    want = str(input("Do you want continue typing new values? [Y/N] ")).strip().upper()
    if want == "Y":
        number = int(input("Type a number: "))
        if average == 1:
            higher = smallest = number
        else:
            if number > higher:
                higher = number
            if number < smallest:
                smallest = number
        sum = sum + number
        length = length + (number / number)
        average = sum / length
    elif want == "N":
        print(" ")
        print("→ The sum between this numbers is {}".format(sum))
        print("→ You typed {:.0f} numbers".format(length))
        print("→ The average between this numbers is {:.1f}".format(average))
        print("→ The higher number was {} and the smallest number was {}".format(higher, smallest))
        print(" ")

# OR

answer = "Y"
sum = amount = average = higher = smallest = 0
while answer in "Yy":
    num = int(input("Type a number: "))
    sum += num
    amount += 1
    if amount == 1:
        higher = smallest = num
    else:
        if num > higher:
            higher = num
        if num < smallest:
            smallest = num
    answer = str(input("Do you want continue? [Y/N] ")).upper().strip()[0]
average = sum / amount
print("→ You typed {} numbers and the average was {}".format(amount, average))
print("→ The higher number was {} and the smallest number was {}".format(higher, smallest))
print("Finish")
