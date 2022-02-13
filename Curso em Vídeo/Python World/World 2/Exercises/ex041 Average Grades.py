"""
Make a code that show a message according to average of student:
Approved
Disapproved
Recuperation
"""

g1 = float(input("First grade: "))
g2 = float(input("Second grade: "))
g3 = float(input("Third grade: "))
average = (g1 + g2 + g3) / 3

if average < 6:
    print("Your average was {:.1f} You are disapproved.".format(average))
    print("Recuperation")
elif average >= 6:
    print("Your average was {:.1f} Congratulation, you are approved.".format(average))


# Or


def school_grades(num):
    grades = []
    total = 0

    for c in range(0, num):
        number = int(input(f"{c+1}º Number: "))
        grades.append(number)
        total += number

    average = total/len(grades)
    print()
    if average < 6:
        print(f"Your average was {average:.1f} You are disapproved. \nRecuperation")
    elif average >= 6:
        print(f"Your average was {average:.1f} You are approved. \nCongratulations.")


school_grades(3)
