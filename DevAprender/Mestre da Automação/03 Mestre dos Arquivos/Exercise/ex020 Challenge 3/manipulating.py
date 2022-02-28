"""
1 - Create 3 lists with:
- 5 fruits
- 5 colors
- 5 programming languages

2 - Create a new file called fruits.txt and add inside it all the fruits in the list
3 - Show on the screen all the lines that are inside the 'fruits.txt' file
4 - Add all the colors to 'fruits.txt' file
5 - Create a new file called 'top 5 languages.txt' and put all languages, one on each line
6 → bonus
 Create a several files using a loop
"""

fruits_list = ["Apple", "Banana", "Watermelon", "Strawberry", "Pineapple"]
colors = ["Red", "Balck", "White", "Gray", "Brown"]
languages = ["Python", "R", "C", "SQL", "Java Script"]

with open('fruits.txt', 'a') as fruits:
    for fruit in fruits_list:
        fruits.write(fruit + '\n')

with open('fruits.txt', 'r') as fruits:
    for line in fruits:
        print(line, end="")

with open('fruits.txt', 'a') as fruits:
    fruits.write("" + '\n')
    fruits.write("Colors:" + '\n')
    for color in colors:
        fruits.write(color + '\n')

with open('top 5 languages', 'a') as top5:
    for lang in languages:
        top5.write(lang + '\n')
