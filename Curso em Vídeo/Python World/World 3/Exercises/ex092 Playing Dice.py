"""
Make a code where 4 players play a dice and get a random result. Save those results in a dictionary in order. And then show the winner.
"""

from random import randint
from time import sleep
from operator import itemgetter

game = {
    'Player1': randint(1, 6),
    'Player2': randint(1, 6),
    'Player3': randint(1, 6),
    'Player4': randint(1, 6)
}

ranking = []

print("Drawn values")

for k, v in game.items():
    sleep(1)
    print(f"{k} took → {v}")
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
# itemgetter(0) order kyes  itemgetter(1) order values
print("=== Player's Ranking ===")
for i, v in enumerate(ranking):
    sleep(1)
    print(f"{i+1}º Place: {v[0]} → {v[1]}")




