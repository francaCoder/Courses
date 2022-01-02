# Primitive Types
# int - Whole Numbers (-3, -2, -1, 0, 1, 2, 3....)
# Float - Real Numbers (50.8, 26.18....)
# Bool - Boolean (True or False)
# Str - Words ("Hello", "7.0"...)
from curses.ascii import isalnum

n1 = input("Type a number: ")
print(type(n1))    # Type = Str

n2 = int(input("Type a number: "))
print(type(n2))    # Type = Int

f1 = float(input("Type a number: "))
print(f1)          # 5.0

b1 = bool(input("Type a value: "))
print(b1)          # Have a value inside? So is 'True', else will be 'False'

Is = input("Type anything: ")
print(Is.isnumeric())   # it does the conversion automatically

alpha = input("Type something: ")
print(alpha.isalpha())  # Alpha = Only letters

#.isalnum()    # Letters and numbers
#.isupper()    # Only capital letters?