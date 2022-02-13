# Improve the previous exercise but now asking how many terms the user still wants to see

firstAP = int(input("First term: "))
reason = int(input("Reason: "))
term = firstAP
counter = 1
total = 0
more = 10
while more != 0:
    total += more
    while counter <= total:
        print("{} →".format(term), end=" ")
        term += reason
        counter += 1
    print("PAUSE")

    more = int(input("How many AP'shortcut you still wants to see? "))
print("AP finished with {} progressions.".format(total))