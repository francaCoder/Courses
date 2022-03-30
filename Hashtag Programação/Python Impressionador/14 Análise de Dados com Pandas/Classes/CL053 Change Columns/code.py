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

# Change date

sales_df['Data da Venda'] = pd.to_datetime(sales_df['Data da Venda'], format="%d/%m/%Y")
print(sales_df.info())

print()
print(sales_df['Data da Venda'])

# Add columns
sales_df['Ano da Venda'] = sales_df['Data da Venda'].dt.year
sales_df['Mes da Venda'] = sales_df['Data da Venda'].dt.month
sales_df['Dia da Venda'] = sales_df['Data da Venda'].dt.day

print(sales_df.info())

print(sales_df['Dia da Venda'])