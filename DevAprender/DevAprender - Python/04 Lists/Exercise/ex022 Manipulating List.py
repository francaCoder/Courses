"""
# 1
Create a list that has the name of 3 objects that you use the most in everyday life, and then show on screen.

# 2
Using just one code line, create a list of 10 at 131

# 3
Print on the screen the result of combination of the list of #1 and #2

# 4
Create lists within lists, which have the names of the 3 objects that you use the most in everyday life, but now within each item, you will add an information, the value of that object.
"""


def show_on_screen(list):
    for item in list:
        print(f"→ {item} ", end="")


objects = ["Computer", "Cell", "Phone"]
show_on_screen(objects)

print()

numbers = list(range(10, 132))
print(numbers)

print()

print(objects + numbers)

print()

main_list = [["Computer"], ["Cell"], ["Phone"]]

print(f"R$5.000,00 → {main_list[0][0]}")
print(f"R$2.500,00 → {main_list[1][0]}")
print(f"R$25,00 → {main_list[2][0]}")

