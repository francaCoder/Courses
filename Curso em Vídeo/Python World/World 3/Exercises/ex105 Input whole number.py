"""
Create a function called wholeNumber() that will do the validation to accept only numbers.
"""


def wholeNumber(msg):
    ok = False
    value = 0
    while True:
        number = str(input(msg)).strip()
        if number.isnumeric():
            value = int(number)
            ok = True
        else:
            print("\033[0;31m[ERROR] Type a valid whole number.\033[m")
        if ok:
            break
    return value


number = wholeNumber("Type a number: ")
print(f"You typed the number → {number}")