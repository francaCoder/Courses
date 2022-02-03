"""
Create a 'while loop' that will keep asking the user the password, the program can only work if the password entered by user is "secret"
"""

password = ""
while password != "Secret":
    password = str(input("type the password: "))
print("Welcome.")