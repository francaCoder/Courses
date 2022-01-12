"""
Make a code that rade the and the gender of several person. For each person registered, the program must ask if the user want continue. At the end show:
- How many peoples are over 18 years old
_ How many men were registered
- How many women are under 20 years old
"""

counter = 1

personsRegistereds = men = over18 = womenUnder20 = 0

while True:
    print("---- {}º Person ----".format(counter))
    name = str(input("Name: "))
    age = int(input("Age: "))
    while age < 1:
        age = int(input("Age: "))
    gender = str(input("Gender: [M/F] ")).strip().upper()[0]
    while gender not in "MF":
        gender = str(input("Gender: [M/F] ")).strip().upper()[0]
    register = str(input("You want register this person? [Y/N] ")).strip().upper()[0]
    while register not in "YN":
        register = str(input("You want register this person? [Y/N] ")).strip().upper()[0]
    if register == "Y":
        personsRegistereds += 1
        counter += 1
        if age >= 18:
            over18 += 1
        if gender == "M":
            men += 1
        if gender == "F" and age < 20:
            womenUnder20 += 1
    wantRegister = str(input("Do you want register more peoples? [Y/N] ")).strip().upper()
    while wantRegister not in "YN":
        wantRegister = str(input("Do you want register more peoples? [Y/N] ")).strip().upper()

    if wantRegister == "N":
        break

print(" ")
print("↓ ↓ ↓ Finish ↓ ↓ ↓")
print("We have {} persons registereds.".format(personsRegistereds))
print("{} men was registereds.".format(men))
print("{} persons has over 18 years old".format(over18))
print("{} women has under 20 years.".format(womenUnder20))




