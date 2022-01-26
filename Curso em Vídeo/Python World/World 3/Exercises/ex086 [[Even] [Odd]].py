"""
Make a code that the user can type 7 numbers and register them in a list with two lists
Even numbers and Odd numbers.
At the end, show the values in ascending order
"""

numbers = [[], []]

for c in range(0, 7):
    number = int(input(f"Type the {c+1}º Number: "))
    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

print(f"Even numbers → {sorted(numbers[0])}")
print(f"Odd Numbers → {sorted(numbers[1])}")