# Playing dices

from random import randint
from time import sleep

while True:
    print("Playing dices...")
    sleep(1.5)
    print(f"Result → {randint(1, 6)}")
    ask = str(input("Do you want to play the dice again? [Y/N] ")).strip().upper()[0]
    while ask not in "YN":
        print("Type just Y or N")
        ask = str(input("Do you want to play the dice again? [Y/N] ")).strip().upper()[0]
    if ask == "N":
        break

# Or


class PlayingDice:
    def __init__(self):
        pass

    def start(self):
        self.PlayDices()

    def PlayDices(self):
        print("Playing dices...")
        sleep(1.5)
        print(f"Result → {randint(1, 6)}")
        ask = str(input("Do you want to play the dice again? [Y/N] ")).strip().upper()[0]
        while ask not in "YN":
            print("Type just Y or N")
            ask = str(input("Do you want to play the dice again? [Y/N] ")).strip().upper()[0]
        if ask == "Y":
            self.PlayDices()
        elif ask == "N":
            print("Thanks.....")


playing_dice = PlayingDice()
playing_dice.start()

