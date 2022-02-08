"""
Make a code that does the computer "think" in a whole number between 0 and 5, and ask
to user if he can answer what was the number chosen by computer
"""

from random import randint
from time import sleep

computer = randint(0, 5)   # Makes the computer think

number = int(input("I will think of a number between 0 and 5, try to guess: "))
print("Processing...")
sleep(1.5)

if number == computer:
    print("Congratulations, you defeated me! :(")
else:
    print("HAHAHA you missed, i thought in {} not in {}".format(computer, number))


# Or


def line(word):
    print(f"-=-=-=-= {word} =-=-=-=-=-")


computer_wins = user_wins = 0

while True:

    computer = randint(0, 5)
    number = int(input("I will think of a number between 0 and 5, try to guess: "))
    while number not in range(0, 5):
        number = int(input("I will think of a number between 0 and 5, try to guess: "))
    print("Processing...")
    sleep(1.5)

    if number == computer:
        user_wins += 1
        print("Congratulations, you defeated me! :(")
    else:
        computer_wins += 1
        print("HAHAHA you missed, i thought in {} not in {}".format(computer, number))

    print(f"Score → Computer: {computer_wins} x User: {user_wins}")
    want_continue = str(input("Do you want to continue playing? [Y/N] ")).strip().upper()[0]
    while want_continue not in "YN":
        want_continue = str(input("Do you want to continue playing? [Y/N] ")).strip().upper()[0]

    if want_continue == "N":
        line("Result")
        if computer_wins > user_wins:
            print(f"Score → Computer: {computer_wins} x User: {user_wins}")
            print("You lost the game, try again latter.")
        elif user_wins > computer_wins:
            print(f"Score → Computer: {computer_wins} x User: {user_wins}")
            print("Yay, congrats! You defeated the computer.")
        else:
            print(f"Score → Computer: {computer_wins} x User: {user_wins}")
            print("The game was draw. Good game.")
        break
