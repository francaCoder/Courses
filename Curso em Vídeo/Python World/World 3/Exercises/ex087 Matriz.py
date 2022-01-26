# Create a matriz with the dimension 3x3 and fill in with the values typed by user

numbers = [[], [], [], [], [], [], [], [], []]

for c in range(0, 9):
    number = int(input(f"Type the {c+1}º Number: "))
    numbers[c].append(number)

print(f"{numbers[0]} {numbers[1]} {numbers[2]}")
print(f"{numbers[3]} {numbers[4]} {numbers[5]}")
print(f"{numbers[6]} {numbers[7]} {numbers[8]}")

# OR

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for line in range(0, 3):
    for column in range(0, 3):
        matriz[line][column] = int(input(f"Type a Number for [{line}, {column}]: "))
print(" ")
for line in range(0, 3):
    for column in range(0, 3):
        print(f"[{matriz[line][column]:^5}]", end="")
    print()

# OR

matriz = [[], [], []]
for line in range(0, 3):
    for column in range(0, 3):
        matriz[line].append(int(input(f"Type a number for [{line},{column}]: ")))
print('-='*20)
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matriz[line][column]:^5}]', end='')
    print()