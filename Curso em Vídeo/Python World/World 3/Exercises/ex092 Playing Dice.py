"""
Make a code where 4 players play a dice and get a random result. Save those results in a dictionary in order. And then show the winner.
"""

from random import randint
from time import sleep
from operator import itemgetter

# game = {
#     'Player1': randint(1, 6),
#     'Player2': randint(1, 6),
#     'Player3': randint(1, 6),
#     'Player4': randint(1, 6)
# }

players = {}
ranking = []

for player in range(0, 4): # 4 = How many players
    players[f'Player {player+1}'] = randint(1, 6)

print("Drawn values")

for player, number in players.items(): # p, n = Player, number
    sleep(1)
    print(f"{player} took → {number}")
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print(ranking)
# itemgetter(0) order kyes  itemgetter(1) order values
print("=== Player's Ranking ===")
for index, player in enumerate(ranking):
    sleep(1)
    print(f"{index+1}º Place: {player[0]} → {player[1]}")







