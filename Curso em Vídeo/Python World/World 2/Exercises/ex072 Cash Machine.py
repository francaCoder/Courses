"""
Make a code that simulate the operation of a cash machine. In the beginning ask to user
what will be the amount to me withdrawn? (Whole number)
The program will inform you how many you will receive

Inside cash machine we have ballots of:
R$1 R$10 R$20 R$50
"""

print("=" * 30)
print("{:^30}".format("França'shortcut Bank"))
print(("=" * 30))

value = int(input("How much money do you want to withdraw? "))
total = value
banknotes = 50
totalBanknotes = 0
while True:
    if total >= banknotes:
        total -= banknotes
        totalBanknotes += 1
    else:
        if totalBanknotes > 0:
            print("{} Banknotes of R${}".format(totalBanknotes, banknotes))
        if banknotes == 50:
            banknotes = 20
        elif banknotes == 20:
            banknotes = 10
        elif banknotes == 10:
            banknotes = 1
        totalBanknotes = 0
        if total == 0:

            break
print("=" * 30)
print("Always come back to França'shortcut Bank. Have a good day!")


# OR


print("=" * 30)
print("{:^30}".format("França'shortcut Bank"))
print(("=" * 30))

value = int(input('How much money do you want to withdraw? R$'))
for banknotes in [50, 20, 10, 1]:
    totalBanknotes = value // banknotes
    value %= banknotes
    if totalBanknotes > 0:
        print(f'{totalBanknotes} Banknotes of R${banknotes}')

print("=" * 30)
print("Always come back to França'shortcut Bank. Have a good day!")


# OR

print("=" * 30)
print("{:^30}".format("França'shortcut Bank"))
print(("=" * 30))

value = int(input("How much money do you want to withdraw? R$"))
banknotes50 = value // 50
value %= 50
print(value)
banknotes20 = value // 20
value %= 20
print(value)
banknotes10 = value // 10
value %= 10
print(value)
banknotes1 = value // 1
print(f"Banknotes of R$50 = {banknotes50}")
print(f"Banknotes of R$20 = {banknotes20}")
print(f"Banknotes of R$10 = {banknotes10}")
print(f"Banknotes of R$1 = {banknotes1}")
print(" ")
print("=" * 30)
print("Always come back to França'shortcut Bank. Have a good day!")
