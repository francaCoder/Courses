import pandas as pd

dados = pd.read_excel("Dados.xlsx")

print(dados['FirstName'].head())

# Selecionando mais de uma coluna

# dados.fillna("Silva", inplace=True)
print(dados[['FirstName', 'MiddleName']])

# Ou printar uma coluna usando a notação de ponto

# print(dados.FirstName)
# Mas não tem como mostrar colunas com espaço no nome desse jeito, e nem mais de uma coluna

# Criando uma nova coluna na nossa tabela

dados['Nome Completo'] = dados['FirstName'] + " " + dados['MiddleName'] + " " + dados['LastName']
print(dados[['FirstName', 'MiddleName', 'Nome Completo']])
