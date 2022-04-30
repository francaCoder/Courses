"""
1 - Select just properties of type = "Apartamento"
2 - Select the properties with the type = "Casa" "Casa de Condomínio", "Casa de Vila"
3 - Select the properties between 60 & 100 m²
4 - Select the properties with 4 bedrooms or more and the rent cost under R$2.000
"""

import pandas as pd

data = pd.read_csv("alugueis_residenciais.csv", sep=";")

selection = data['Tipo'] == "Apartamnto"
print(selection.shape[0])

# n1 = data[selection.shape[0]]
