"""
Read a whole number and show on screen the 'n' first elements of a fibonacci
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

n = int(input("How many terms do you want show? "))
t1 = 0
t2 = 1
print("{} → {}".format(t1, t2), end=" ")
counter = 3
while counter <= n:
    t3 = t1 + t2
    print("→ {}".format(t3), end=" ")
    t1 = t2
    t2 = t3
    counter += 1
print("→ End")