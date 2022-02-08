"""
The same teacher want draw the presentation order.
Make a code that read the name of 4 students and show the order drawn
"""

from random import shuffle


n1 = str(input("First name: "))
n2 = str(input("Second name: "))
n3 = str(input("Third name: "))
n4 = str(input("Fourth name: "))

orderedList = [n1, n2, n3, n4]
shuffle(orderedList)

print("The order will be:")
print(orderedList)

# Or


def presentation(how_many_students=1):
    students = []
    for c in range(0, how_many_students):
        students.append(str(input(f"{c+1}º Name: ")))
    print("The order will be:")
    shuffle(students)
    print(students)


presentation(5)


# Or


students = []

while True:
    student = str(input(f"Student's Name: ")).strip().title()
    save = str(input("Do you want to save this student? [Y/N] ")).strip().upper()[0]
    while save not in "YN":
        save = str(input("Do you want to save this student? [Y/N] ")).strip().upper()[0]
    if save == "Y":
        students.append(student)
    want_continue = str(input("Do you want to continue? [Y/N] ")).strip().upper()[0]
    while want_continue not in "YN":
        want_continue = str(input("Do you want to continue? [Y/N] ")).strip().upper()[0]

    if want_continue == "N":
        shuffle(students)
        break

print("The presentation order will be:")
print(students)


