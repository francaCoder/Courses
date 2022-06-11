import pandas as pd
import numpy as np

# Especificando qual aba abrir

df = pd.read_excel("Dados Excel.xlsx", sheet_name="Plan1")
# df = pd.read_excel("Dados Excel.xlsx", sheet_name="Aba2")

print(df)

# Vendo quais são as abas do meu arquivo excel

file = pd.ExcelFile("Dados Excel.xlsx")

print(file.sheet_names) # ['Plan1', 'Aba2']

aba1 = file.parse("Plan1")
aba2 = file.parse("Aba2")

print(aba1.head())