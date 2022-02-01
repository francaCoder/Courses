"""
Make a program that has a function called grades() that can receive several student'shortcut grades and will return a dictionary with the following informations:

- How many grades
- The higher grade
- The smaller grade
- The class'shortcut average
- The situation[optional]
"""


def grades(* grade, situation=False):
    """
    => Analyze grades and the class'shortcut situation
    :param grade: Several grades
    :param situation: Optional parameter
    :return: A Dictionary
    """
    classroom = {
        'Total': len(grade),
        'Higher Number': max(grade),
        'Average': sum(grade) / len(grade)
    }
    if situation:
        if classroom['Average'] >= 6:
            classroom['Situation'] = "Good"
        else:
            classroom['Situation'] = "Bad"
    return classroom



answer = grades(5.5, 2.5, 1.5, situation=True)
print(answer)
