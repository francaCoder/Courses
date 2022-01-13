"""
Make a code that read 5 numbers and save them in a list.
At the end, show which was the higher and the smallest number typed and also show tha positions in list.
"""

counter = 1
values = []
# higherNumber = 0
# smallestNumber = 0

for n in range(0, 5):
    # number = int(input(f"Put a number in {counter}º position: "))
    # values.append(number)
    # if n == 0:
    #     higherNumber = smallestNumber = values[n]
    # else:
    #     if values[n] > higherNumber:
    #         higherNumber = values[n]
    #         if values[n] < smallestNumber:
    #             smallestNumber = values[n]
    values.append(int(input(f"Put a number in {counter}º position: ")))
    counter += 1

print(" ")
print(f"You typed the values {values}")
print(f"The highest number was {max(values)} in position {values.index(max(values))+1}.")
# for i, v in enumerate(values):
#     if v == max(values):
#         print(f"{i+1}...")
print(f"The smallest number was {min(values)} in position {values.index(min(values))+1}.")
# for i, v in enumerate(values):
#     if v == min(values):
#         print(f"{i+1}...")
