"""
Make an interactive help. The user will type a method and will appear the manual according to the method entered by user. Whe the user type "End" the program will close.
"""

# command = ""
# while True:
#     command = str(input("Function or Library > "))
#     if command.upper() == "FIM":
#         break
#     else:
#         help(command)
#

# OR
from time import sleep

colors = (
    "\033[m",         # 0 - None
    "\033[0;30;41m",  # 1 - Red
    "\033[0;30;42m",  # 2 - Green
    "\033[0;30;44m",  # 3 - Blue
    "\033[7;30m",     # 4 - White
)


def helping(com):
    title(f'Accessing the << {com} >> manual', 2)
    sleep(1.5)
    print(colors[4], end="")
    help(com)
    print(colors[0], end="")


def title(msg, color=0):
    length = len(msg) + 4
    print(colors[color], end="")
    print("~"*length)
    print(f"  {msg}  ")
    print("~"*length)
    print(colors[0], end="")


command = ""
while True:
    title("PyHELP SYSTEM", 3)
    command = str(input("Function or Library > "))
    if command.upper() == "FIM":
        break
    else:
        helping(command)
title("<< See you later! >>", 1)