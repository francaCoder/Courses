import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("alugueis_residenciais.csv", sep=';')
#
# data = data.fillna({"Condominio": 0, "IPTU": 0})
#
# print(data['Valor'].mean())

# Calculete the average rent for each neighborhood

print(data['Bairro'])
neighborhoods = ["Botafogo", "Jacarepaguá", "Méier", "Leblon", "Copacabana"]

selection = data['Bairro'].isin(neighborhoods)

data = data[selection]

neighborhoods_group = data.groupby('Bairro')

# print(neighborhoods_group.groups)

for bairro, index in neighborhoods_group:
    print(f"The average rent in {bairro} is R${index['Valor'].mean():.2f}")

neighborhoods_group = neighborhoods_group[["Valor", "Condominio"]].mean().round(2)

print(neighborhoods_group)

print(neighborhoods_group['Valor'].describe().round(2))

print(neighborhoods_group['Valor'].aggregate(['min', 'max', 'sum']))