import pandas as pd

dataframe = pd.read_csv("Contoso - Vendas  - 2017.csv", sep=";")

print(dataframe)

# Filter Columns
print()
print(dataframe['Quantidade Vendida'])

# Filter lines
print()
print(dataframe[:3]) # [3 rows x 10 columns]

# 3 Columns
print()
print(dataframe[["Numero da Venda", "Data da Venda", "Quantidade Vendida"]])
# [980642 rows x 3 columns]

# Show the Amount sale (01/01/2017 line 0)
print()
print(dataframe['Quantidade Vendida'][0]) # 9

# Show the Amount sale (01/01/2017 line 2)
print(dataframe['Quantidade Vendida'][2]) # 13
