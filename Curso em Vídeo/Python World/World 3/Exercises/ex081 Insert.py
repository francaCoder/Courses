"""
Create a program where the user can type 5 numbers and save them in a list, already in correct position
(Don't use the .sort())
At the end show the ordered list
"""

values = []

for n in range(0, 5):
    number = int(input("Type a number: "))
    if n == 0 or number > values[-1]:
        values.append(number)
        print("Added to end of list...")
    # if n == 0:
    #     values.append(number)
    # elif n > values[-1]:   →  If the number is greater than the number in the last element
    #     values.append(n)

    else:
        pos = 0
        while pos < len(values):
            if number <= values[pos]:
                values.insert(pos, number)
                print(f"Added to position {pos} of list...")
                break
            pos += 1

print(" ")
print(f"The values typed in ascending order were {values}")