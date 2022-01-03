"""
Create a program that read the full name entered by user and show:

- The name with all letters in upper
- The name with all letters in lower
- How many letters have the name not counting the spaces
- How many letters have the first name

"""

name = str(input("Type your full name: ")).strip()
"""
separateName = name.split()
hml = len(separateName[0]) + len(separateName[1]) + len(separateName[2]) + len(
    separateName[3])
    
print("You full name have {} letters.".format(hml))
print(("Your first name have {} letters.".format(len(separateName[0]))))    
"""

print("Your name in Uppercase is {}.".format(name.upper()))
print("Your name in Lowercase is {}.".format(name.lower()))
print("Your full name have {} letters.".format(len(name) - name.count(" ")))
print("Your first name have {} letters.".format(name.find(" ")))
