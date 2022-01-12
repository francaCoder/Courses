"""
Make a code that read 4 values from keyboard and put them in a tuple, and then show:
- How many times appear the number 9
- What's the position of the first number 3
- Which was the Even Numbers?
"""

numbers = (int(input("First Number: ")),
           int(input("Second Number: ")),
           int(input("Third Number: ")),
           int(input("Fourth Number: ")),
           )

print(f"You typed the values → {numbers}")
print("The number 9 appear {} times.".format(numbers.count(9)))
if 3 in numbers:
    print("The first number three is in {}ª position.".format(numbers.index(3)+1))
print("The values entered were → ", end="")
for n in numbers:
    if n % 2 == 0:
        print(n, end=" ")