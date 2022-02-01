"""
Make a program that has a function called token(), that receive two option parameters:
- The football player'shortcut name
- How many goals he scored

working even if any parameter isn't fill in.
"""


def token(name="<< Unknown >>", goals=0):
    if goals > 1:
        print(f"{name} scored {goals} goals.")
    elif goals == 1:
        print(f"{name} scored {goals} goal.")
    elif goals == 0:
        print(f"{name} don't scored goal.")


token()
