# Read and checking the gender [M/F]. If the answer is wrong, can a new answer.

gender = str(input("What'shortcut your gender? [M/F] ")).strip().upper()[0]
while gender not in "MF":
    gender = str(input("Invalid datas, please inform your gender [M/F] ")).strip().upper()[0]
print("Gender saved successfully.")

#OR

gender = ["M", "F"]
while gender[0] == "M" or gender[0] == "F":
    g = str(input("What'shortcut your gender? [M/F] ")).strip().upper()
    if g != gender[0] and g != gender[1]:
        print("Invalid value.")

#OR

m = "M"
f = "F"
while not m or f:
    g = str(input("What'shortcut your gender? [M/F] ")).strip().upper()
    if g != m and g != f:
        print("Invalid Value")


