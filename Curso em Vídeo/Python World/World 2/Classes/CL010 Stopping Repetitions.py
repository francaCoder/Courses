"""
Break
"""

counter = 1
while True: # Forever
    print(counter, "→ ", end="")
    counter += 1
print("End")
print(" ")


n = s = 0
while n != 999:
    n = int(input("Type a number: "))
    s += n
s -= 999
print("The sum is worth {}".format(s))
print("End")
print(" ")


# Infinity loop

n = s = 0
while True:
    n = int(input("Type a number: "))
    if n == 999:
        break
    s += n
print("The sum is worth {}".format(s))
