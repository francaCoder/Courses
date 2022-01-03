"""
The maximum speed of the track is 80km/h
The traffic ticket will cost R$7,00 per Km/h
"""

vel = int(input("What's the current velocity? "))
# km = vel * 7
# km = vel * 7 - 560  (560 = 80 * 7)
# km = (vel - 80) * 7


if vel > 80:
    print("The maximum velocity of track is 80Km/h")
    print(f"You were fined and must pay R${km},00")
    print("Drive carefully!")
else:
    print("Have a good trip and Drive carefully!")