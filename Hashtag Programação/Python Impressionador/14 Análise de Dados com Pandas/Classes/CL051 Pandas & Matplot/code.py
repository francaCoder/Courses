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


# Which costumer bought the most?

frequency_costumers = sales_df['E-mail do Cliente'].value_counts()
# print(frequency_costumers)

mpl.plot(frequency_costumers[:5])

# frequency_costumers[:5].plot(figsize=(15, 5), yticks=range(0, 100, 5)) → Não mostrou nada

mpl.show()


# Which store bought the most?

sales_store = sales_df.groupby('Nome da Loja').sum()

sales_store = sales_store.sort_values('Quantidade Vendida', ascending=False)
print(sales_store[['Quantidade Vendida']])

mpl.plot(sales_store[:5])
mpl.show()