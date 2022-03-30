import pandas as pd
import matplotlib.pyplot as mpl

sales_df = pd.read_csv("Contoso - Vendas  - 2017.csv", sep=";")
products_df = pd.read_csv("Contoso - Cadastro Produtos.csv", sep=";")
store_df = pd.read_csv("Contoso - Lojas.csv", sep=";")
clients_df = pd.read_csv("Contoso - Clientes.csv", sep=";")

clients_df = clients_df[["ID Cliente", "E-mail"]]
products_df = products_df[["ID Produto", "Nome da Marca"]]
store_df = store_df[["ID Loja", "Nome da Loja"]]

sales_df = sales_df.merge(products_df, on="ID Produto")
sales_df = sales_df.merge(store_df, on="ID Loja")
sales_df = sales_df.merge(clients_df, on="ID Cliente")

sales_df = sales_df.rename(columns={"E-mail": "E-mail do Cliente"})

print(sales_df.info())


"""
If i want to create a table just with the sales of 'Loja Contoso Europe Online' that had no returned sale, and then show how many sales are.
"""


store306 = sales_df[sales_df['ID Loja'] == 306]
no_returned = sales_df['Quantidade Vendida'] == 0

dataframe_2 = sales_df[store306, no_returned]

print(dataframe_2)

