list1 = ["A", "B", "C", "D", "E"]
list2 = [1, 2, 3, 4, 5]

for a, b in zip(list1, list2):
    print(f"{a} → {b} /", end="")

# Zip looks like enumerate


products = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]
prices = [250, 150, 220, 550, 50]

for a, b in zip(products, prices):
    print(f"{a} → R${b:.2f}")


# And if the length of a list is shorter than the other
from itertools import zip_longest

titles = ["Title1", "Title2", "Title3", "Title4"]
descriptions = ["Description 1", "Description 2", "Description 3"]

for title, description in zip_longest(titles, descriptions):
    print(f"We found the {title} with description {description}.")

# Title 4 receive 'none'
