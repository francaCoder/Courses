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
    print("Your average was {} . You are disapproved.".format(average))
    print("Recuperation")
elif average >= 6:
    print("Your average was {} . Congratulation, you are approved.".format(average))
