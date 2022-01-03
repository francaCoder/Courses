"""
In all languages, we need use conditions to do differents codes according to values,
numbers, ways entereds by user

Using If and else

if .... :
'do this'
-
-
-
else:
'do this'
-
-
-
"""

name = str(input("What's your name? ")).strip()
if name == "Matheus":
    print("Your name's beautiful")
else:
    print("Your name is so ugly")
print("Welcome, {}".format(name))



n1 = float(input("First note: "))
n2 = float(input("Second note: "))
average = (n1 + n2) / 2
print("Your average was {}".format(average))
if average >= 6:
    print("Congratulations, you have been approved!")
else:
    print("You got a low grade, you will have no cell phone")

# OR
# print("Good note" if average >=6 else "Bad note")


