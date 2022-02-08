internet = None

try:
    print("Making the connection with " + internet)
except TypeError as error:
    print("Unable to complete your purchase, check your internet connection")
finally:
    print("Undoing your purchase")


#

try:
    number = int(input("Type a number: "))
    print(number/0)
except ZeroDivisionError as error:
    print("Cannot divide by 0")
except ValueError as error:
    print("Just type numbers")
finally:
    print("Operation canceled")
