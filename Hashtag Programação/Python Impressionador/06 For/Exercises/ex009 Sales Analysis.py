"""
We have a list with sellers and sales. Show which was the sellers that reached the goal and the sales amount.
"""

goal = 1000
sales = [
    ["João", 800],
    ["Júlia", 1200],
    ["Marcos", 700],
    ["Maria", 1000],
    ["Ana", 1100],
    ["João", 900],
]

for seller in sales:
    if seller[1] >= goal:
        print(f"The selle {seller[0]} sold {seller[1]}")