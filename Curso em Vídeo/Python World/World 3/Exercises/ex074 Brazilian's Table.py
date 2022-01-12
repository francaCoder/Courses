"""
Create a tuple filled with the top 20 teams in the Brazilian's championship table, and then show:
- Only the top 5
- The last 4 placed
- A list with all teams in alphabetical order
- What's the position of Chapecoense according to table?
"""

teams = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense")
print("-="*15)
print(f"Teams's list → {teams}")
print("-="*15)

#Top five
print("Top five teams → {}".format(teams[:5]))
print("-="*15)

# Last 4
print("The last 4 teams → {}".format(teams[-4:]))
print("-="*15)


# Alphabetical order
print("Teams in alphabetical order → {}".format(sorted(teams)))
print("-="*15)

# Chapecoense's position
print("The Chapecoense is in {}ª position.".format(teams.index("Chapecoense") + 1))
