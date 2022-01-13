"""
Create a program where the user can type several numbers and save them in a list.
Case the number already exist, he can't be added.
At the end show the numbers in ascending order
"""

values = []

while True:
    number = int(input("Type a number: "))
    while number in values:
        number = int(input("Duplicate value, I will not continue. Another Number: "))
    print("Save successfully..")
    values.append(number)
    wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    if wantContinue == "N":
        print("End")
        break

print(" ")
print(f"You typed the values → {sorted(values)}")

# OR

numbers = []
while True:
    n = int(input("Type a value: "))
    if n not in numbers:
        numbers.append(n)
        print("Save Successfully...")
    else:
        print("Duplicate value, I will not continue.")
    r = str(input("Do you want continue? [Y/N] "))
    if r in "Nn":
        break


print("-=" * 30)
print(f"You typed the values {numbers}")