"""
Make a code that play with the computer. The game will be interrupted only when the user lost,
showing the total consecutive wins
"""


from random import randint
from time import sleep

userWins = 0
computerWins = 0

while True:
    userChoice = str(input("What's your choice - Even or Odd? [E/O] ")).strip().upper()[0]
    while userChoice not in "EO":
        userChoice = str(input("What's your choice - Even or Odd? [E/O] ")).strip().upper()[0]
    computerNumber = randint(0, 10)
    if userChoice == "E":
        userNumber = int(input("Choice a Number: "))
        print("Even or...")
        sleep(1)
        print("Odd")
        sleep(0.6)
        if (userNumber + computerNumber) % 2 == 0:
            userWins += 1
            print("You choose {} and the computer choose {} Total → {} →".format(userNumber, computerNumber, userNumber + computerNumber), end= " ")
            print("Even Number" if (userNumber + computerNumber) % 2 == 0 else "Odd Number")
            print("Score → User {} x Computer {}".format(userWins, computerWins))
        else:
            computerWins += 1
            print("You choose {} and the computer choose {} Total → {} →".format(userNumber, computerNumber, userNumber + computerNumber), end= " ")
            print("Even Number" if (userNumber + computerNumber) % 2 == 0 else "Odd Number")
            print("The Score → User {} x Computer {}".format(userWins, computerWins))
            break
    elif userChoice == "O":
        userNumber = int(input("Choice a Number: "))
        print("Even or...")
        sleep(1)
        print("Odd")
        sleep(0.6)
        if ((userNumber + computerNumber) % 2) != 0:
            userWins += 1
            print("You choose {} and the computer choose {} Total → {} →".format(userNumber, computerNumber, userNumber + computerNumber), end= " ")
            print("Even Number" if (userNumber + computerNumber) % 2 == 0 else "Odd Number")
            print("Score → User {} x Computer {}".format(userWins, computerWins))
        else:
            computerWins += 1
            print("You choose {} and the computer choose {} Total → {} →".format(userNumber, computerNumber, userNumber + computerNumber), end= " ")
            print("Even Number" if (userNumber + computerNumber) % 2 == 0 else "Odd Number")
            print("The Score → User {} x Computer {}".format(userWins, computerWins))
            break

# OR

userWins = 0

while True:
    user = int(input("Type a number: "))
    computer = randint(0, 10)
    total = user + computer
    choice = str(input("Even or Odd? [E/O] ")).strip().upper()[0]
    while choice not in "EO":
        choice = str(input("Even or Odd? [E/O] ")).strip().upper()[0]
    print("You choose {} and the computer choose {}. Total → {} →".format(user, computer, total), end=" ")
    print("Even Number" if total % 2 == 0 else "Odd Number")
    if choice == "E":
        if total % 2 == 0:
            userWins += 1
            print("You won!")
        else:
            print("You lost!")
            break
    elif choice == "O":
        if total % 2 == 1:
            userWins += 1
            print("You won!")
        else:
            print("You lost!")
    print("Let's play again...")
print("GAME OVER! You won {} times.".format(userWins))
