import pandas as pd

df = pd.read_csv("bank.csv", sep=";")

# Selecionar colunas

# Dentro de array [[]]


#filter
print(df.filter(items=["job", "Marital"]).head())


# Like - Algumas letras que contém na coluna

print() # Default
print(df.filter(like="ult").head())

print() # Marital / Contact
print(df.filter(like="ta").head())

# Regex

print(df.filter(regex=".day.").head())