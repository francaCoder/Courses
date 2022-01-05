"""
nested conditions = More options, streets, ways, etc.
IF / ELSE / ELIF
"""

name = str(input("What's your name? "))
if name == "Matheus":
    print("Your name's so beautiful...")
elif name == "Pedro" or name == "João" or name == "Maria":
    print("Your name's very popular in brazil.")
else:
    print("Your name's normal")
print("Have a good day, {}!".format(name))
