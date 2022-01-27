"""
Make a code where 4 players play a dice and get a random result. Save those results in a dictionary in order. And then show the winner.
"""

from random import randint
from time import sleep

ranking = [[], [], [], []]

players = {'Player1': randint(1, 6), 'Player2': randint(1, 6), 'Player3': randint(1, 6), 'Player4': randint(1, 6)}

for player, number in players.items():
    sleep(1)
    print(f"{player} took → {number}")
    if player == "Player1":
        ranking[0] = "Player1"


sleep(1)
print("Ranking")

print(ranking)





