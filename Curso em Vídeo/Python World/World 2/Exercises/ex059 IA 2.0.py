# Redo the IA exercise, but now showing how many attempts did it took to beat the computer

from random import randint
from time import sleep

computerWins = 0
userWins = 0
yes = "Y"
while yes == "Y":
    ask = str(input("Do you want try beat the computer? [Y/N] ")).strip().upper()
    computer = randint(0, 5)  # Makes the computer think
    print(computer)
    if ask == yes:
        number = int(input("C0MPUT3R: Ok, I will think of a number between 0 and 5, try to guess: "))
        print("Processing...")
        sleep(1.5)
        print(" ")
        if number == computer:
            userWins += 1
            print("C0MPUT3R: Congratulations, you defeated me! :(")
            print("The score is Computer {} x User {}".format(computerWins, userWins))
            if computerWins > userWins:
                print("C0MPUT3R: I'm winning of you hahaha, you're so weak....")
            elif computerWins == userWins:
                print("We are draw!")
            else:
                print("C0MPUT3R: I didn't think you were so good.")
        else:
            computerWins += 1
            print("HAHAHA you missed, i thought in → {} not in → {}".format(computer, number))
            if computerWins > userWins:
                print("i thought you were better HAHA")
            elif computerWins == userWins:
                print("we are draw, try again and see if you can win...")
            else:
                print("I will reach you, don't run away from the battle")
            print("The score is Computer {} x User {}".format(computerWins, userWins))
        print(" ")

    if ask == "N":
        print("Medroso")

# OR

from random import randint
computer = randint(0, 10)
print("I'm your computer... I Thought in a number between 0 and 10.")
print("Try to guess the number.")
win = False
tries = 0
while not win:
    user = int(input("Choice a number: "))
    tries += 1
    if user == computer:
        win = True
    elif user < computer:
        print("More...Try again")
    elif user > computer:
        print("Less...Try again")
print("You used {} tries, congratulations!".format(tries))


