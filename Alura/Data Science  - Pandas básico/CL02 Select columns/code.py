import pandas as pd

# External Files

employees_df = pd.read_csv("CadastroFuncionarios.csv", sep=";", index_col=2)
print(employees_df.head()) # Top 5

print()
print()

# Especific column
print(employees_df["Cargo"])

print(type(employees_df["Cargo"])) # <class 'pandas.core.series.Series'

new_df = employees_df[["Cargo"]]
print(new_df)
print(type(new_df)) # <class 'pandas.core.frame.DataFrame'>

print()
print(new_df[:3]) # First 3 Lines
print()

# Loc - Names
print(employees_df.loc['Gabriel Mesquita'])

# 2 Lines
print(employees_df.loc[['Gabriel Mesquita', 'João Haddad']])

# Columns
print(employees_df.loc[['Gabriel Mesquita', 'João Haddad'], ['ID Funcionário', 'Area']])

print()

# Iloc - Index
print(employees_df.iloc[0])
# Dataframe:
print(employees_df.iloc[[0]])

# Lines & Columns
print(employees_df.iloc[1:4, [0, 4, 2]])