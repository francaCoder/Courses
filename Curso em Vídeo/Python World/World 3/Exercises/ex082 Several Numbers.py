"""
Make a code that will read several numbers and save them in a list.
After this show:
- How many numbers was typed
- The list ordering in descending order
- Whether or not 5 is on the list
"""


values = []
howManyNumbers = 0
while True:
    number = int(input("Type a number: "))
    values.append(number)
    howManyNumbers += 1
    wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    if wantContinue == "N":
        print("End")
        break

values.reverse()

print(f"You typed {howManyNumbers} numbers.")
print(f"The values in descending order is {values}")
if 5 in values:
    print(f"The number 5 was find in list in position {values.index(5)+1}")
else:
    print("The number 5 don't was find in list.")

