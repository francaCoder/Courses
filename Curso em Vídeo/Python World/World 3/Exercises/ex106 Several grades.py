"""
Make a program that has a function called grades() that can receive several student's grades and will return a dictionary with the following informations:

- How many grades
- The higher grade
- The smaller grade
- The class's average
- The situation[optional]
"""


def studentGrades(* grades, situation=None):
    higher = max(grades)
    smaller = min(grades)
    classAverage = sum(grades) / len(grades)


studentGrades(1, 2, 3, 4, 5, 6)
print(hig)