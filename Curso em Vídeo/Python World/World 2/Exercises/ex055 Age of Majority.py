# Read when 7 peoples was born and answer which one hasn't yet reached the age of majority


from datetime import date


for c in range(0, 7):
    year = int(input("When you was born? "))
    currentYear = date.today().year
    sum = currentYear - year
    if sum >= 21:
        print("You reached the age of majority.")
    else:
        print("Still {} years to you reached the age of majority.".format(21 - sum))

#OR


currentYear = date.today().year
totalBiggest = totalSmallest = 0
for person in range(1, 8):
    wasBorn = int(input("In which year the {}ª people was born? ".format(person)))
    age = currentYear - wasBorn
    if age >= 21:
        totalBiggest += 1
    else:
        totalSmallest += 1

print("Altogether we had {} peoples of legal age.".format(totalBiggest))
print("And also, we had {} peoples underage.".format(totalSmallest))

