# Read a number and answer if it is a prime number or no

number = int(input("Type a number: "))
total = 0
for c in range(1, number + 1):
    if number % c == 0:
        total += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print("{}".format(c), end=' ')

print("\n\033[m0 The number {} was divided {} times.".format(number, total))

if total == 2:
    print("It is a prime number.")
else:
    print("It isn't a prime number.")
