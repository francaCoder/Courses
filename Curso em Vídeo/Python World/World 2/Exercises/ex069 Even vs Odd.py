"""
Make a code that play with the computer. The game will be interrupted only when the user lost,
showing the total consecutive wins
"""

from random import randint
from time import sleep

wantPlay = "Y"
userWins = 0
computerWins = 0

while computerWins < 1:
    userChoice = str(input("What's your choice - Even or Odd? [E/O] ")).strip().upper()[0]
    while userChoice not in "EO":
        userChoice = str(input("What's your choice - Even or Odd? [E/O] ")).strip().upper()[0]
    computerNumber = randint(0, 10)
    print("Computer choose {}".format(computerNumber))
    if userChoice == "E":
        userNumber = int(input("Choice a Number: "))
        print("Even or...")
        sleep(1)
        print("Odd")
        sleep(0.6)
        if (userNumber + computerNumber) % 2 == 0:
            userWins += 1
            print("The Score is → User {} x Computer {}".format(userWins, computerWins))
        else:
            computerWins += 1
            print("The Score → User {} x Computer {}".format(userWins, computerWins))
    elif userChoice == "O":
        userNumber = int(input("Choice a Number: "))
        print("Even or...")
        sleep(0.6)
        print("Odd")
        sleep(0.2)
        if ((userNumber + computerNumber) % 2) != 0:
            userWins += 1
            print("The Score is → User {} x Computer {}".format(userWins, computerWins))
        else:
            computerWins += 1
            print("The Score → User {} x Computer {}".format(userWins, computerWins))
    elif computerWins == 1:
        if userWins == 1:
            print("Congratulations, you won 1 time.")
            print("But the game finished.")
        elif userWins > 1:
            print("Congratulations, you won {} times in a row.".format(userWins))
            print("But the game finished.")
        else:
            print("C0MPUT3R → You are so weak...")
        break
