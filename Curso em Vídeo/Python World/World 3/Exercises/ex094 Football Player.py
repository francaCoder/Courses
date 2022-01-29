"""
Create a program that manages the data of a football player.
The program will read how many matches did he play and then will read how many goals were scored in each match. And in the end, everything will be saved in a dictionary, including total goals
"""

player = {}
matches = []
player['Name'] = str(input("Name: "))
total = int(input(f"How many matches did {player['Name']} play: "))
for c in range(0, total):
    matches.append(int(input(f"How many goals in the {c}º match? ")))
player['Goals'] = matches[:]
player['Total'] = sum(matches)
print("-="*30)
print(player)
print("-="*30)
for k, v in player.items():
    print(f"{k} → {v}")
print("-="*30)
print(f"The player {player['Name']} played {len(player['Goals'])} matches.")
for i, v in enumerate(player['Goals']):
    print(f"   => Int the {i}º game did {v} goals.")
print(f"The total goals was → {player['Total']}")

#OR

player = {}

player['Name'] = str(input("Name: "))
player['Matches'] = int(input(f"How many matches did {player['Name']} play: "))
player['Goals'] = []

for i in range(0, player['Matches']):
    player['Goals'].append(int(input(f"How many goals in the {i+1}º match? ")))
player['Total'] = sum(player['Goals'])

print('-=' * 30)
print(player)
print('-=' * 30)

for k, v in player.items():
    print(f"{k} → {v}")

print('-=' * 30)
if player['Matches'] > 1:
    print(f"{player['Name']} played {player['Matches']} matches.")
else:
    print(f"{player['Name']} played {player['Matches']} match.")

for c in range(0, player['Matches']):
    if player['Goals'][c] > 1:
        print(f"   => In the {c+1}º match scored {player['Goals'][c]} goals.")
    else:
        print(f"   => In the {c+1}º match scored {player['Goals'][c]} goal.")

if player['Goals'][c] > 1:
    print(f"And the total of goals were → {player['Goals'][c]}.")
else:
    print(f"The total was only {player['Goals'][c]} goal.")

# Or

player = {}

player['Name'] = str(input("Name: "))
player['Matches'] = int(input(f"How many matches did {player['Name']} play: "))
player['Goals'] = []

for c in range(0, player['Matches']):
    player['Goals'].append(int(input(f"Goals int the {c+1}º Match: ")))
player['Total'] = sum(player['Goals'])

print(f"The player {player['Name']} scored {player['Total']} goals in {player['Matches']} matches.")
for k, v in enumerate(player['Goals']):
    print(f'{k+1}º Match → {v} goals')



