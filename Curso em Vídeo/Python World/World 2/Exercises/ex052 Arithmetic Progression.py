# Read the first term of AP and show the first 10 terms of that progression

firstAP = int(input("First term: "))
reason = int(input("Reason: "))
ten = firstAP + (10 - 1) * reason

for c in range(firstAP, ten + reason, reason):
    print(c)
print("Finished")