"""
How to create and modify files:
'r' → read (Read something)
'w' → write (Write something)
'r+' → (Read and write something)
'a' → add (add something)
"""

cell_prices = [850, 2230, 1500, 3500, 5000]
other_prices = [245, 757]
plans = [
    "Plan 50mb basic",
    "Plan 100mb medium",
    "Plan 200mb plus",
]

with open('cell_phone_values.txt', 'w') as file:
    for price in cell_prices:
        file.write(str(price) + '\n')

with open('cell_phone_values.txt', 'r') as file:
    for plan in file:
        print(plan)

with open('cell_phone_values.txt', 'a') as file:
    for price in other_prices:
        file.write(str(price) + '\n')

with open('cell_phone_values.txt', 'r') as file:
    for line in file:
        print(line)

with open('cell_phone_values.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write("Finish...")