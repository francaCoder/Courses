import pandas as pd

dados = pd.read_excel("Dados.xlsx")
# dados.set_index("FirstName", inplace=True)

# Linha - Coluna
# O loc é pelo nome do valor

print(dados.loc[0:3])
   # BusinessEntityID PersonType  NameStyle  ...    LastName Suffix EmailPromotion
# 0                 1         EM          0  ...     Sánchez    NaN              0
# 1                 2         EM          0  ...       Duffy    NaN              1
# 2                 3         EM          0  ...  Tamburello    NaN              0
# 3                 4         EM          0  ...     Walters    NaN              0
print()
print(dados.loc[[1, 3, 4]])
#    BusinessEntityID PersonType  NameStyle  ...  LastName Suffix EmailPromotion
# 1                 2         EM          0  ...     Duffy    NaN              1
# 3                 4         EM          0  ...   Walters    NaN              0
# 4                 5         EM          0  ...  Erickson    NaN              0
print()
print(dados.loc[[9, 17, 23], ["FirstName", "MiddleName"]])
   # FirstName MiddleName
# 9    Michael        NaN
# 17      John          L
# 23      Jill          A


# Iloc é por número
print(dados.iloc[2:4])

print(dados.iloc[2:4, 4:6])
  # FirstName MiddleName
# 2   Roberto        NaN
# 3       Rob        NaN


# E posso selecionar colunas usando True ou False dentro do array