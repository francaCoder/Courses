"""
# 1
Create a function called → Generate_full_name that receive as parameter the name and surname and welcome that person
"""


def generate_full_name(name="<< Unknown >>", surname="<< Unknown >>"):
    print(f"Welcome, {name} {surname}!")


generate_full_name("Matheus", "França")

# or

generate_full_name(name=str(input("Name: ")), surname=str(input("Surname: ")))