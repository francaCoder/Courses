"""
Improve the last exercise showing:

- The sum between all even numbers
- The sum of third column
- The highest number of second line
"""

numbers = [[], [], [], [], [], [], [], [], []]
even = 0

for c in range(0, 9):
    number = int(input(f"Type the {c+1}º Number: "))
    numbers[c].append(number)

print("-="*20)
print(f"{numbers[0]} {numbers[1]} {numbers[2]}")
print(f"{numbers[3]} {numbers[4]} {numbers[5]}")
print(f"{numbers[6]} {numbers[7]} {numbers[8]}")
print("-="*20)

for n in numbers:
    if n[0] % 2 == 0:
        even += n[0]

highest = max(numbers[3][0], numbers[4][0], numbers[5][0])

print(f"The sum between the even numbers is {even}.")
print(f"The sum of the third column is {numbers[2][0] + numbers[5][0] + numbers[8][0]}.")
print(f"The highest number of second line is {highest}.")


# OR

evenSum = highest = columnSum = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for line in range(0, 3):
    for column in range(0, 3):
        matriz[line][column] = int(input(f"Type a Number for [{line}, {column}]: "))
print(" ")
for line in range(0, 3):
    for column in range(0, 3):
        print(f"[{matriz[line][column]:^5}]", end="")
        if matriz[line][column] % 2 == 0:
            evenSum += matriz[line][column]
    print()

print(f"The sum of even numbers is {evenSum}.")
for line in range(0, 3):
    columnSum += matriz[line][2]
print(f"The sum of values of third column is {columnSum}.")
for c in range(0, 3):
    if c == 0:
        highest = matriz[1][c]
    elif matriz[1][c] > highest:
        highest = matriz[1][c]
print(f"The highest value of second line is {highest}.")