"""
CHALLENGE 1

Use the necessary operation(Continue || Break) for the following condition to occur:
- When arriving at "Rap" it shouldn't be shown on screen
musical_genres = ["Hip-Hop", "Rock", "Rap", "Pop"]


CHALLENGE 2
Use the necessary operation(Continue || Break) For the following condition occur:
- When arriving at "Rock" the program must be interrupted.
musical_genres = ["Hip-Hop", "Rock", "Rap", "Pop"]
"""

musical_genres = ["Hip-Hop", "Rock", "Rap", "Pop"]

# 1
for genre in musical_genres:
    if genre == "Rap":
        continue
    print(genre)

print()

# 2
for genre in musical_genres:
    if genre == "Rock":
        break
    print(genre)