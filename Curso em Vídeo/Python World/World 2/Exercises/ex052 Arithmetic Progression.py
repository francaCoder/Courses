# Read the first term of AP and show the first 10 terms of that progression

firstAP = int(input("First term: "))
reason = int(input("Reason: "))
term = firstAP
counter = 1
while counter <= 10:
    print("{} → ".format(term), end=" ")
    term += reason
    counter += 1
print("End")