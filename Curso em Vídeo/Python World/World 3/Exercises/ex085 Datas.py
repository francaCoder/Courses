"""
Make a code that read the name and the weight of several peoples, save all in a list.
And then show:

- How many peoples were registered
- The heaviest and the lighter people
"""

secondList = []
mainList = []
less = greater = 0

while True:
    secondList.append(str(input("Name: ")))
    secondList.append(float(input("Weight: ")))
    if len(mainList) == 0:
        less = greater = secondList[1]
    else:
        if secondList[1] > greater:
            greater = secondList[1]
        if secondList[1] < less:
            less = secondList[1]
    mainList.append(secondList[:])
    secondList.clear()

    wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    if wantContinue == "N":
        break

print(" ")
print(f"Were registered {len(mainList)} people.")
print(f"The greater weight was {greater}Kg. Weight of →", end=" ")
for p in mainList:
    if p[1] == greater:
        print(f"[{p[0]}]", end=" ")
print()
print(f"The less weight was {less}Kg. Weight of →", end=" ")
for p in mainList:
    if p[1] == less:
        print(f"[{p[0]}]", end=" ")
print()



# for weight in list:
#     totalWeight.append(peso[1])
#
# greaterWeight = max(totalWeight)
# lessWeight = min(totalWeight)
