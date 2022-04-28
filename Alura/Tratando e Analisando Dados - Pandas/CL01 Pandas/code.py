import pandas as pd

rent_df = pd.read_csv("aluguel.csv", sep=';')
print(rent_df.info())

# print(rent_df.head())

data_type = pd.DataFrame(rent_df.dtypes, columns=['Tipos de Dados'])

data_type.columns.name = "Variávies"

print(data_type)

# Line & Columns
# (32960, 9)
print(rent_df.shape)