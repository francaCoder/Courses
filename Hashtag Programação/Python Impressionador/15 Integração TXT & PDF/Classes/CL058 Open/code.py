"""
Using open, you can open a file .txt or .pdf
"""

from pprint import pprint

file = open("students", "r")

# r = Read
# w = Create/Write
# a = add/append

# print(file.read())
# Just show

# print(file.readlines())
# Modify each element in your file to index of a list


# Write / Create

file = open("test", "w")

file.write("Hello, my name's Matheus")

file.close()
