goal = 1000

sales = [
    ["João", 700],
    ["Edu", 1100],
    ["Lucas", 900],
    ["Matheus", 800],
    ["Isaac", 1000],
    ["Bruno", 1200],
]

# I want to know which was the seller's % that reached the goal

# 1
winners = []

for seller in sales:
    if seller[1] >= goal:
        winners.append(seller)

print(f"{len(winners) / len(sales):.0%} of sellers reached the goal")


# 2

winners = 0

for seller in sales:
    if seller[1] >= goal:
        winners += 1

print(f"{winners / len(sales):.0%} of sellers reached the goal")


# Who was the best seller?

amount = []
name = []
for seller in sales:
    amount.append(seller[1])

for seller in sales:
    if seller[1] == max(amount):
        name = seller[0]

print(f"The best seller was {name}")

#

name = ""
amount = 0

for seller in sales:
    if seller[1] > amount:
        amount = seller[1]
        name = seller[0]

print(f"The best seller was {name} and sold R${amount}")