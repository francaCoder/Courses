import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# cotacao_ibov = web.DataReader("^BVSP", data_source="yahoo", start="2020-01-01", end="2020-11-10")

wallet = pd.read_excel("Carteira.xlsx")

cotacoes_carteira = pd.DataFrame()

for ativo in wallet['Ativos']:
    print(ativo)
    cotacoes_carteira[ativo] = web.DataReader(f"{ativo}.SA", data_source="yahoo", start="2020-01-01", end="2020-11-10")['Adj Close'] # Só essa coluna

print(cotacoes_carteira.info())
print(cotacoes_carteira.iloc[0])

# Tratar o ativo 'XPLG11' que está com 110 dados enquanto os outros ativos estão com 215

# Podemos excluir as linhas vazias, preencher com a média, preencher com o valor anterior....


# 1
df_media = cotacoes_carteira.mean()

cotacoes_carteira.fillna(df_media, inplace=True)

# Nesse caso, ele já entende que ele vai preencher com a média nos valores daquele ativo com dados faltantes e não vai interferir nos outros

# Ou

# cotacoes_carteira = cotacoes_carteira.ffill() # ffill, preenche com o valor anterior



# Agora temos que criar cotações normalizadas, porque as cotações começam e terminam em valores muitos distantes, impossibilitando a gente de fazer comparações. O ideal seria que elas começassem no mesmo ponto.

# vamos pegar os valores de cotação e dizer que o valor de referência é sempre o valor inicial, para sabermos percentualmente quanto subiu ou caiu

# Pega todos e divide pelo primeiro

carteira_norm = cotacoes_carteira / cotacoes_carteira.iloc[0] # só [0] são os cabeçalhos, temos que usar o iloc

carteira_norm.plot(figsize=(15, 5))

# plt.legend(loc='upper left') # Legenda no canto esquerdo em cima
plt.show()

# IBOV x Carteira

cotacao_ibov = web.DataReader("^BVSP", data_source="yahoo", start="2020-01-01", end='2020-11-10')

# temos que comparar quanto que o ibovespa rendeu e quanto que a nossa carteira rendeu. Mas precisamos lembrar que além dos ativos terem preços diferentes, nós temos quantidades diferentes de cada ativo, então cada coluna de cada ativo, eu vou multiplicar o valor dele pela quantidade que eu tenho.

valor_investido = pd.DataFrame()

# for ativo in wallet['Ativos']:
#     valor_investido[ativo] = cotacoes_carteira[ativo] * wallet.loc[wallet['Ativos'] == ativo, "Qtde"].values[0]
    # Loc = Linha / coluna, quero localizar a linha da carteira em que na coluna de ativos é igual o ativo do meu for, e depois eu pedo o valor da coluna de quantidade
    # Esse loc me gerou um DataFrame de um item só, por exemplo, ativo mglu3 vai aparecer      2   1000
    # 2 da linha e 1000 da quantidade. Eu preciso desse número 1000 pra multiplicar, então, sempre quando tiver um DataFrame de apenas um valor, podemos colocar no final .values[0] que ele vai te retornar o primeiro valor

# Ou dessa forma que é mil vezes mais fácil
for i, ativo in enumerate(wallet['Ativos']):
    valor_investido[ativo] = cotacoes_carteira[ativo] * wallet['Qtde'][i]

print(valor_investido.info())
print(valor_investido)


# Comparação - Carteira x Ibov

# Vou criar uma coluna de  total na tabela de valor investido, essa coluna vai receber o próprio df.sum(), porém no axis=1, para somar a LINHA do dia, não a coluna

valor_investido['Total'] = valor_investido.sum(axis=1)

print(valor_investido['Total'])
print(cotacao_ibov['Adj Close'])


# Como a nossa carteira performou
valor_investido['Total'].plot(figsize=(15, 5), label="Carteirinha")

# Agora precisamos saber como que ele foi em relação ao índice bovespa
cotacao_ibov['Adj Close'].plot(label="Ibov")

# Precisamos normalizar os dois

valor_investido_norm = valor_investido / valor_investido.iloc[0]
cotacao_ibov_norm = cotacao_ibov / cotacao_ibov.iloc[0]

valor_investido_norm['Total'].plot(figsize=(15, 5), label="Carteirinha")

cotacao_ibov_norm['Adj Close'].plot(label="Ibov")



plt.legend()
plt.show()

# Podemos ver que o ibovespa começou maior que a nossa carteira e terminou menor, ou seja, nossa carteira rendeu mais do que o ibovespa

# Retorno de cada um

retorno_carteira = valor_investido['Total'][-1] / valor_investido['Total'][0] - 1
retorno_ibov = cotacao_ibov['Adj Close'][-1] / cotacao_ibov['Adj Close'][0] - 1

print(f"{retorno_carteira:.2%}")
print(f"{retorno_ibov:.2%}")

# Correlação dos dois
correlacao = valor_investido['Total'].corr(cotacao_ibov['Adj Close'])
print(correlacao)