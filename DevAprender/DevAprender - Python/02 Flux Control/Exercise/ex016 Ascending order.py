# Create a 'while loop' that count and print on screen starting from 100 and ending in 1.

counter = 100
while counter >= 1:
    print(counter)
    counter -= 1
print("Finish")

# Or

for c in range(counter, 0, -1):
    print(c)
print("Finish")