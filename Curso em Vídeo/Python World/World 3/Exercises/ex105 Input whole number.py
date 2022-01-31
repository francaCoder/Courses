"""
Create a function called wholeNumber() that will do the validation to accept only numbers.
"""


def wholeNumber(validation):
    while type(validation) != type(0):
        print("oi")


wholeNumber(validation=int(input("Number: ")))