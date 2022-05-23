import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web

quotes_df = pd.read_excel("Carteira.xlsx")
# print(quotes_df)

# for company in quotes_df['Ativos']:
#     quote = web.DataReader(f"{company}", data_source='yahoo', start='2020-01-01', end='2020-11-10') # Year, Month, Day

# Dataframe de cotações dos ativos da certeira
quotes_wallet = pd.DataFrame()
for company in quotes_df['Ativos']:
    # print(company)
    quotes_wallet[company] = web.DataReader(f"{company}.SA", data_source='yahoo', start='2020-01-01', end='2020-11-10')['Adj Close'] # Year, Month, Day

print(quotes_wallet.info())

#2 adjusting data
# df_average = quotes_wallet.mean()
# quotes_wallet.fillna(df_average, inplace=True)
#
# print(quotes_wallet.info())

# or
# quotes_wallet.ffill(inplace=True)
# # Preenche com o número anterior
#
# print(quotes_wallet.info())

# 3

# normal_wallet = quotes_wallet / quotes_wallet.iloc[0]
# normal_wallet.plot(figsize=(15, 5))
#
# plt.legend(loc='upper left')
# plt.show()
#
# print(quotes_wallet.iloc[0])

# Pull the IBOV's quote to start

ibov_wallet = web.DataReader("^BVSP", data_source="yahoo", start="2020-01-01", end="2020-11-10") # Year, Month, Day
print(ibov_wallet)

# Criando um dataframe da carteira com as quantidades de ações

carteira = pd.read_excel('Carteira.xlsx')
valor_investido = pd.DataFrame()

cotacoes_carteira = pd.DataFrame()

for ativo in carteira['Ativos']:
    cotacoes_carteira[ativo] = web.DataReader('{}.SA'.format(ativo), data_source='yahoo', start='2020-01-01', end='2020-11-10')['Adj Close']

for ativo in carteira['Ativos']:
    valor_investido[ativo] = cotacoes_carteira[ativo] * carteira.loc[carteira['Ativos']==ativo, 'Qtde'].values[0]
# Carteira x IBOV

valor_investido['Total'] = valor_investido.sum(axis=1)
# print(valor_investido)

valor_investido_norm = valor_investido / valor_investido.iloc[0]
cotacao_ibov_norm = ibov_wallet / ibov_wallet.iloc[0]

valor_investido_norm['Total'].plot(figsize=(15, 5), label='Carteira')
cotacao_ibov_norm['Adj Close'].plot(label='IBOV')
plt.legend()
plt.show()

# Wallet Return / Ibov Return

wallet_return = valor_investido['Total'][-1] / valor_investido['Total'][0] -1
ibov_return = ibov_wallet['Adj Close'][-1] / ibov_wallet['Adj Close'][0] -1

print(f"Wallet → {wallet_return:.2%}")
print(f"IBOV → {ibov_return:.2%}")