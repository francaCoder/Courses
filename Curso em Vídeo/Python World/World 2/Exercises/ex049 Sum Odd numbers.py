# Calculate the sum of all odd numbers that are multiples of 3 between 1 and 500

sum = 0
counter = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        counter += 1
        sum += c
print("The sum between all {} values is {}".format(counter, sum))