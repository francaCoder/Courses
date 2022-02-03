# Continue = Jump
# Break = stop

for number in range(100):
    if number % 2 == 0:
        print(number)
    else:
        continue # Jump

print()

for number in range(10):
    print(number)
    if number == 5:
        break