import pandas as pd

data = pd.read_csv("alugueis_residenciais.csv", sep=';')

print(data.head(10))

print(data.info())
print(data.isnull())

print()
print(data[data['Valor'].isnull()])

A = data.shape[0]
data.dropna(subset=['Valor'], inplace=True)
B = data.shape[0]

print(A - B)

print(data.info())

# 2

selection = (data['Tipo'] == "Apartamento") & (data['Condominio'].isnull())
A = data.shape[0]
data = data[~selection]
B = data.shape[0]

print(A - B)

data.fillna(0, inplace=True)
data = data.fillna({"Condominio": 0, "IPTU": 0})

print(data.info())