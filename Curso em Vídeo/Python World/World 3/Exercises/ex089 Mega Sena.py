"""
Make a code that helps the user to create guesses for Mega Sena.
The program will ask how many games will be made and then will draw 6 numbers between 1 and 60
for each game, registered all in one composite list.
"""

from random import randint
from time import sleep

list = []
games = []
print("-="*20)
print("               Mega Sena")
print("-="*20)

times = int(input("How many games do you want me to draw? "))
total = 1
while total <= times:
    counter = 0
    while True:
        num = randint(1, 60)
        if num not in list:
            list.append(num)
            counter += 1
        if counter >= 6:
            break

    list.sort()
    games.append(list[:])
    list.clear()
    total += 1

print(" ")
print("-="*3, f"DRAWING {times} GAMES", "-="*3)
sleep(1)
for i, l in enumerate(games):
    print(f"Game {i+1}: {l}")
    sleep(1)
print("-="*5, "< Good Luck! >", "-="*5)


# OR

from random import randint
from time import sleep

print('-=' * 20)
print(f'{"MEGA SENA":^40}')
print('-=' * 20)
games = int(input('How many games do you want me to draw? '))
print(f'=-=-=-=  DRAWING {games} GAMES  =-=-=-=')
sleep(1)
for c in range(0, games):
    game = []
    while len(game) != 6:
        number = randint(1, 60)
        if number not in game:
            game.append(number)
    print(f'{c+1}º Game: {sorted(game)}')
    sleep(1)
print('=-=-=-=-= < Good Luck! > =-=-=-=-=')
