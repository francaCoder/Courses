# Nested loops
# Country + state


countries = ["Brazil", "EUA", "Germany", "Russia", "Italy"]
seasons = ["Spring", "Summer", "Autumn", "Winter"]

for country in countries:
    for season in seasons:
        print(f"{country} → {season}")