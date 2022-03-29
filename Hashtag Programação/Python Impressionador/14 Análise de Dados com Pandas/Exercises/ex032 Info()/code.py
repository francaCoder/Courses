import pandas as pd

dataframe = pd.read_csv("Contoso - Vendas  - 2017.csv", sep=";")

print(dataframe.info())

clients_list = dataframe['ID Cliente']
print()
print(clients_list)

# Stock

print()
products_stock = ["ID Produto", "Quantidade Vendida", "Quantidade Devolvida"]
products_stock = dataframe[products_stock]
print(products_stock)