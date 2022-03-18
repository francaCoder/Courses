"""
Your program should verify the CO2's concentration in several places. According to level, check if that place is safe
"""
from pprint import pprint
from random import randint

states = {
    "AC": [randint(250, 550) for c in range(5)],
    "AL": [randint(250, 550) for c in range(5)],
    "AP": [randint(250, 550) for c in range(5)],
    "AM": [randint(250, 550) for c in range(5)],
    "BA": [randint(250, 550) for c in range(5)],
    "CE": [randint(250, 550) for c in range(5)],
    "ES": [randint(250, 550) for c in range(5)],
    "GO": [randint(250, 550) for c in range(5)],
    "MA": [randint(250, 550) for c in range(5)],
    "MT": [randint(250, 550) for c in range(5)],
    "MS": [randint(250, 550) for c in range(5)],
    "MG": [randint(250, 550) for c in range(5)],
    "PA": [randint(250, 550) for c in range(5)],
    "PB": [randint(250, 550) for c in range(5)],
    "PR": [randint(250, 550) for c in range(5)],
    "PE": [randint(250, 550) for c in range(5)],
    "PI": [randint(250, 550) for c in range(5)],
    "RJ": [randint(250, 550) for c in range(5)],
    "RN": [randint(250, 550) for c in range(5)],
    "RS": [randint(250, 550) for c in range(5)],
    "RO": [randint(250, 550) for c in range(5)],
    "RR": [randint(250, 550) for c in range(5)],
    "SC": [randint(250, 550) for c in range(5)],
    "SP": [randint(250, 550) for c in range(5)],
    "SE": [randint(250, 550) for c in range(5)],
    "TO": [randint(250, 550) for c in range(5)],
    "DF": [randint(250, 550) for c in range(5)],
}

normal_level = 350
maximum_level = 450

# pprint(states)

for state in states:
    sensors = len(states[state])
    total_co2 = sum(states[state])
    average = total_co2 / sensors
    if average > maximum_level:
        print(f"{state} is with a high level of CO2 ({average}), it's not safe")