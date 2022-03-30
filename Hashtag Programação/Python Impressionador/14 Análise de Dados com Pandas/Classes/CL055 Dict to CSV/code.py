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

products_sales = {
    "Iphone": [56451, 15641],
    "Galaxy": [14894, 48691]
}

# sales_df.to_csv("Novo Vendas 2017.csv", sep=";")

products_df = pd.DataFrame.from_dict(products_sales, orient="index")
products_df = products_df.rename(columns={
    0: "2019 Sales",
    1: "2020 Sales",
})
print(products_df)