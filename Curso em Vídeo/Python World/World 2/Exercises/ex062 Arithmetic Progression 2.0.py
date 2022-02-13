"""
Redo the 'AP exercise' using the while
"""

firstAP = int(input("First term: "))
reason = int(input("Reason: "))
term = firstAP
counter = 1
while counter <= 10:
    print("{} → ".format(term), end=" ")
    term += reason
    counter += 1
print("End")