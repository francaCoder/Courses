"""
Fix the indentation of this code:

import time


def thinkFor10Seconds():
    print("Thinking...")
    time.sleep(10)
    print("Remembered!")


if 10 > 5:


print("Yes")

class welcome():
        def __init__(self):
print("Welcome")

hello = welcome()
"""

import time


def thinkFor10Seconds():
    print("Thinking...")
    time.sleep(10)
    print("Remembered!")


if 10 > 5:
    print("Yes")

class welcome:
    def __init__(self):
        print("Welcome")


hello = welcome()