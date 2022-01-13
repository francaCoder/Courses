"""
Make a code that read several numbers and save them in list.
And then, create 2 lists, the first will receive the Even Numbers and the second the Odd Numbers.
At the end, show the 3 lists
"""

values = []
evenNumbers = []
oddNumbers = []


while True:
    number = int(input("Type a number: "))
    values.append(number)
    if number % 2 == 0:
        evenNumbers.append(number)
    else:
        oddNumbers.append(number)

    wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    if wantContinue == "N":
        print("End")
        break

print(" ")
print(f"The numbers typed were → {values}")
if len(evenNumbers) > 1:
    print(f"The Even Numbers typed were → {evenNumbers}")
else:
    print(f"The Even Number typed was → {evenNumbers} ")
if len(oddNumbers) > 1:
    print(f"The Odd Numbers typed were → {oddNumbers}")
else:
    print(f"The odd Number typed was → {oddNumbers}")