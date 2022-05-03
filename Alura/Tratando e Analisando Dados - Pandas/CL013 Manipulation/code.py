import pandas as pd
s = pd.Series(list("bcudwiamcsnjchaspiscja"))

print(s)

print(s.unique())

print(s.value_counts())

df = pd.read_csv("aluguel.csv", sep=";")

print(df.info())

print(df.Tipo.unique())

print(df.Tipo.value_counts())