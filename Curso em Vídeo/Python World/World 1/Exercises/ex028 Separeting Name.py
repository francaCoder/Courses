"""
Make a code that read person's full name and then displays the first on the console name
and then the second name

"""

name = str(input("Type your full name: ")).strip()
separateName = name.split()

print("Your first name is {}".format(separateName[0]))
print("Your last name is {}".format(separateName[len(separateName) - 1]))

