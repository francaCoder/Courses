import pandas as pd

df = pd.read_csv("bank.csv", sep=";")

print(df.info())

# Somente o que são solteiros
print(df[df['marital'] == "single"].head())

# Somente o que são solteiros e educação primária
print(df[(df['marital'] == "single") & (df['education'] == "primary")])

# Pegando a idade e o trabalho dessas pessoas
new_df = df[(df['marital'] == "single") & (df['education'] == "primary")]

# print(new_df[['age', 'job']]) # 1
# Ou
print(new_df.iloc[:, [0, 1]])


# Usando o operador OU

# Quero que a pessoa seja solteira e tenha educação secundária ou terciária
# Obrigatóriamente solteiro e o nível de educação pode mudar
print((df['marital'] == "single") & ((df['education'] == 'secondary') | (df['education'] == 'tertiary')))

solteirinhos_df = df[(df['marital'] == "single") & ((df['education'] == 'secondary') | (df['education'] == 'tertiary'))]

print(solteirinhos_df)
