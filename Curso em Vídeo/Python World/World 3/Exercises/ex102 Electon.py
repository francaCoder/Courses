"""
Create a program that has a function called vote() that will receive the year of birth as parameter, returning if this person must vote or no.
"""


def vote(yearOfBirth):
    """
    => Will show if the user must vote or no.
    :param yearOfBirth: When the user was born
    :return: No return
    """
    from datetime import datetime
    age = datetime.now().year - yearOfBirth
    print(f"You has {age} years old.")

    if age < 16:
        print("Can't vote.")
    elif age < 18:
        print("Optional vote.")
    elif age < 65:
        print("Mandatory vote.")
    else:
        print("Optional vote")


vote(yearOfBirth=int(input("When you was born? ")))