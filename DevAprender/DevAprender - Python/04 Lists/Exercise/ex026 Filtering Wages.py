"""
Using the list below, filter only vacancies with wage over R$2500
"""

vacancies = [
    ["Vacancy 1", 1200],
    ["Vacancy 2", 2550],
    ["Vacancy 3", 5000]
]


def over_wage(vacancy):
    if vacancy[1] >= 2500:
        return True
    else:
        return False


print(list(filter(over_wage, vacancies)))
