import pandas as pd

# Read File

# sales_df = pd.read_csv("Contoso - Cadastro Produtos.csv")
sales_df = pd.read_csv("Contoso - Vendas  - 2017.csv", sep=";")
# I need pass the separator

# Dataframe - Table


print(sales_df)