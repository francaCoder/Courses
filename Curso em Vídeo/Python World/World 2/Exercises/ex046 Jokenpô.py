"""
Make the computer play 'jokenpô' with you.
"""

from random import randint
from time import sleep
import emoji

choices = ("Rock", "Paper", "Scissor")

computer = randint(0, 2)

print("Try to beat computer")
print("""Make your choice
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissor """)
user = int(input("What's your move? "))

sleep(0.7)
print("Jo...")
sleep(0.7)
print("ken...")
sleep(0.7)
print("PÔ!!")

if computer == 0 and user == 2:
    print("Computer won and User lost, Rock breaks Scissor")
elif computer == 1 and user == 0:
    print("Computer won and User lost, Paper wraps Rock")
elif computer == 2 and user == 1:
    print("Computer won and User lost, Scissor cut Paper")

if user == 0 and computer == 2:
    print("User won and Computer lost, Rock breaks Scissor")
elif user == 1 and computer == 0:
    print("User won and Computer lost, Paper wraps Rock")
elif user == 2 and computer == 1:
    print("User won and Computer lost, Scissor cut Paper")

if user != 0 and user != 1 and user != 2:
    print(""" Invalid move, which: 
    [ 0 ] Rock 
    [ 1 ] Paper
    [ 2 ] Scissor
    """)

elif user == computer:
    print("The game was a draw, play again")



