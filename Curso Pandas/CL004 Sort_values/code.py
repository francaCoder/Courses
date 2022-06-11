import pandas as pd

df = pd.read_excel("Dados.xlsx", usecols=['FirstName', 'MiddleName', 'LastName'])

print(df.head())
print()

# Ordenar pelo nome

print(df.sort_values("FirstName").head())
print()

# Posso ordenar por mais de uma coluna, passando dentro de um array


# > pro < e < pro >
print(df.sort_values("FirstName", ascending=False).head())
print()

