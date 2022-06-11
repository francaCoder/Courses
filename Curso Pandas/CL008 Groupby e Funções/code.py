import pandas as pd

df = pd.read_csv("bank.csv", sep=';')

# Média de idade da rapaziada
print(df.age.mean())

# Média da idade das pessoas casadas
casadas_df = df.loc[df['marital'] == 'married', :]
print(casadas_df['age'].mean())

# ou

print(df[df.marital == "married"].age.mean())

# Groupby

# filtrei as colunas, agrupei por 'marital' e tirei a média da outra coluna que é a idade
print(df[['marital', 'age']].groupby(['marital']).mean())

# média das pessoas que são casadas e tem educação primária
new_df = df.loc[(df['marital'] == "married") & (df['education'] == 'primary')]
print()
print(new_df.age.mean())

# Média do balanço de pessoas com idade entre 30 e 50, casadas e separadas
colunas = ["balance", "marital"]

balanco = df[((df.age >= 30) & (df.age <= 50)) & (df.marital.isin(['married', 'divorced']))][colunas].groupby('marital').mean()

print(balanco)