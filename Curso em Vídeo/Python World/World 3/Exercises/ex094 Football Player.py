"""
Create a program that manages the data of a football player.
The program will read how many matches did he play and then will read how many goals were scored in each match. And in the end, everything will be saved in a dictionary, including total goals
"""

footballPlayer = {"Name": str(input("Name: ")), "Matches": int(input("How many matches: "))}
for m in range(0, footballPlayer['Matches']):
    footballPlayer["Goals"] = int(input(f"How Many goals he score in the {m+1} match?"))
print(footballPlayer)

footballPlayer = []
data = {"Name": str(input("Name: ")), "Matches": int(input("How many matches: ")), "Goals": [[], [], [], [], ]}
for m in range(0, data['Matches']):




