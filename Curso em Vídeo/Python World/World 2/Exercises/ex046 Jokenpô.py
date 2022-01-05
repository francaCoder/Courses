"""
Make the computer play 'jokenpô' with you.
"""

from random import choice
from time import sleep
import emoji

choices = ["ROCK", "PAPER", "SCISSOR"]

computer = choice(choices)
print(computer)

print("Try to beat computer")
user = str(input("'Rock' / 'Paper' / 'Scissor' ? ")).strip().upper()
sleep(0.7)
print("Jo...")
sleep(0.7)
print("ken...")
sleep(0.7)
print("PÔ")

if computer == "ROCK" and user == "SCISSOR":
    print("Computer won and User lost, Rock breaks Scissor")
elif computer == "PAPER" and user == "ROCK":
    print("Computer won and User lost, Paper wraps Rock")
elif computer == "SCISSOR" and user == "PAPER":
    print("Computer won and User lost, Scissor cut Paper")

if user == "ROCK" and computer == "SCISSOR":
    print("User won and Computer lost, Rock breaks Scissor")
elif user == "PAPER" and computer == "ROCK":
    print("User won and Computer lost, Paper wraps Rock")
elif user == "SCISSOR" and computer == "PAPER":
    print("User won and Computer lost, Scissor cut Paper")

if user != "ROCK" and user != "SCISSOR" and user != "PAPER":
    print("Invalid move, which 'Rock', 'Paper or 'Scissor'")
elif user == computer:
    print("The game was a draw, play again")


