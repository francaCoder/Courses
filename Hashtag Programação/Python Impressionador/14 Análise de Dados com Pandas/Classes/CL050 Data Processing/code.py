import pandas as pd

# dataframe = pd.read_csv("Contoso - Cadastro Produtos.csv")
sales_df = pd.read_csv("Contoso - Vendas  - 2017.csv", sep=";")
products_df = pd.read_csv("Contoso - Cadastro Produtos.csv", sep=";")
store_df = pd.read_csv("Contoso - Lojas.csv", sep=";")
clients_df = pd.read_csv("Contoso - Clientes.csv", sep=";")

# print(clients_df.info())

# print(sales_df)
# print("→→→→")
# print(products_df)
# print("→→→→")
# print(store_df)
# print("→→→→")
# print(clients_df['E-mail'])


# Remove Columns

# clients_df = clients_df.drop(["Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10"], axis=1)
# Axis=1 → Columns
# Axis=0 → Lines


# I just want some columns
clients_df = clients_df[["ID Cliente", "E-mail"]]
# print(clients_df)

# print(products_df.info())
products_df = products_df[["ID Produto", "Nome da Marca"]]

# print(store_df.info())
store_df = store_df[["ID Loja", "Nome da Loja"]]

sales_df = sales_df.merge(products_df, on="ID Produto")
sales_df = sales_df.merge(store_df, on="ID Loja")
sales_df = sales_df.merge(clients_df, on="ID Cliente")

# print(sales_df)

# Rename columns

sales_df = sales_df.rename(columns={
    "E-mail": "E-mail do Cliente",
    # "Numero da Venda": "Example"
})
print(sales_df)