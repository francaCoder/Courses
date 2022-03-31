"""
Now, imagine that the store called 'Loja Contoso Roma' (ID 222), tried to cheat the system, took 1 out of each returned sale that he had
"""

import tqdm
import pandas as pd
import openpyxl

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

# for item in sales_df:
#     print(item)

pbar = tqdm(total=len(sales_df['ID Loja']))


for index, id in enumerate(sales_df['ID Loja']):
    if id == 222:
        sales_df.loc[index, "Quantidade Devolvida"] += 1
        pbar.update()

print(sales_df['Quantidade Devolvida'])
