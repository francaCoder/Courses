"""
Improve the "ex94 Football player" so that it work with several players, including a system viewing details of each player's performance
"""

team = []
player = {}
matches = []

while True:
    player.clear()
    player['Name'] = str(input("Name: "))
    total = int(input(f"How many matches did {player['Name']} play: "))
    matches.clear()
    for c in range(0, total):
        matches.append(int(input(f"How many goals in the {c+1}º match? ")))
    player['Goals'] = matches[:]
    player['Total'] = sum(matches)
    team.append(player.copy())
    # while True:
    #     answer = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    #     if answer in "YN":
    #         break
    #     print("[ERROR] Please, type just Y to Yes or N to no")
    # if answer == "N":
    #     break
    wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        print("[ERROR] Please, type just Y to Yes or N to no")
        wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    if wantContinue == "N":
        break

print(player)
print(team)
print("-="*30)
print("Cod ", end="") # Alignment
for element in player.keys(): # Alignment
    print(f"{element:<15}", end="") # Alignment
print()
print("-"*40)

for k, v in enumerate(team):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-="*30)
while True:
    search = int(input("Show the data of which player? [999 to Stop]"))
    if search == 999:
        break
    if search >= len(team):
        print(f"[ERROR] Don't exist player with code {search}")
    else:
        print(f" -- DATA OF PLAYER {team[search]['Name']} -- ")
        for index, goals in enumerate(team[search]['Goals']):
            print(f"   In the {index}º match scored {goals} goals.")
    print("-"*40)
print("<< ALWAYS BACK >>")


