"""
Make a code that has a tuple with the name and the price in sequence.
At the end, show a price's listing, organizing the datas in tabular form
"""
listing = (
            "Pencil", 1.75,
            "Eraser", 2,
            "Journal", 15.90,
            "Pencil case", 25,
            "Scale", 4.20,
            "Compass", 9.99,
            "Bag", 120.32,
            "Sharpener", 2.20,
            "Book", 34.90
           )
print("_" * 40)
print(f'{"PRICE LISTING":^40}')
print("_" * 40)

for element in range(0, len(listing)):
    if element % 2 == 0:
        print(f"{listing[element]:.<30}", end="")
    else:
        print(f"R${listing[element]:>7.2f}")
print("_" * 40)