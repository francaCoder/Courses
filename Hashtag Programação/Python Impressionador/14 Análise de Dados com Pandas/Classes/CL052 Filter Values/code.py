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


# What's the sales' %?

sales_amount = sales_df['Quantidade Vendida'].sum()
amount_returned = sales_df['Quantidade Devolvida'].sum() # 138931


# .sum():

# total = 0
# for item in sales_df['Quantidade Devolvida']:
#     total += item
#
# print(total)


print(sales_amount)
print(amount_returned)
print(f"{amount_returned/sales_amount:.2%}") # → 1.17%


# If i want to do this something just for the store called 'Loja Contoso Europe Online'?

# print(sales_df[['ID Loja', 'Nome da Loja']])
sales_contoso_store = sales_df[sales_df['ID Loja'] == 306]
# print(sales_contoso_store[['ID Loja', "Quantidade Vendida", "Quantidade Devolvida"]])

sales_amount = sales_contoso_store['Quantidade Vendida'].sum()
amount_returned = sales_contoso_store['Quantidade Devolvida'].sum()

print(f"{amount_returned/sales_amount:.2%}") # 1.33%


# Or

is_store306 = sales_df['ID Loja'] == 306
print(is_store306)

sales_contoso_store = sales_df[is_store306]
