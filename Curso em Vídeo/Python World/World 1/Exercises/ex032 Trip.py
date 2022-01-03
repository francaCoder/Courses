"""
Create a code that ask the distance of a trip in Km
- Each Km/h cost R$0.50 for trips from up to 200 Km and R$0,45 for trips above 200 Km
"""

distance = float(input("What's the distance in Km? "))
far = distance * 0.45
close = distance * 0.50

if distance <= 200:
    print(f"The total to pay is R${close}")
else:
    print(f"The total to pay is R${far}")