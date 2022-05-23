import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web

wallet = pd.read_excel("CarteiraMentoria.xlsx")
# print(wallet)

ibov_df = web.DataReader("^BVSP", data_source="yahoo", start='2020-01-01', end='2020-12-10')
print(ibov_df.info())

ibov_df['Adj Close'].plot()
plt.show()

#

wallet_df = pd.DataFrame()
remove = ["Tesouro Selic", "VVAR3"]

for ativo in wallet['Ativos']:
    if ativo not in remove:
        wallet_df[ativo] = web.DataReader(f"{ativo}.SA", data_source="yahoo", start='2020-01-01', end='2020-12-10')['Adj Close']

print(wallet_df)
print(wallet_df.info())
# wallet_df = wallet_df.ffil()
#
# print(wallet_df)

tesouro_df = pd.read_csv("https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv", sep=';', decimal=',')

tesouro_df['Data Base'] = pd.to_datetime(tesouro_df['Data Base'], format='%d/%m/%Y')
print(tesouro_df.info())
print(tesouro_df)

tesouro_df = tesouro_df.loc[tesouro_df['Tipo Titulo'] == "Tesouro Selic", :]
print(tesouro_df)

# Merge - Tesouro Selic - Wallet
tesouro_df = tesouro_df.rename(columns={"Data Base": "Date"})
wallet_df = wallet_df.merge(tesouro_df[['Date', 'PU Base Manha']], on='Date', how='left')
wallet_df = wallet_df.ffill()
print(wallet_df)

# Qual é o valor investido

valor_investido = wallet_df.copy()

for ativo in wallet['Ativos']:
    if ativo not in remove:
        valor_investido[ativo] = valor_investido[ativo] * wallet.loc[wallet['Ativos'] == ativo, 'Qtde'].values[0]

valor_investido = valor_investido.set_index('Date')
valor_investido['Total'] = valor_investido.sum(axis=1)
print(valor_investido)
print(valor_investido.info())

valor_investido_norm = valor_investido / valor_investido.iloc[0]
ibov_norm = ibov_df / ibov_df.iloc[0]

valor_investido_norm['Total'].plot(figsize=(15, 5), label='Wallet')
ibov_norm['Adj Close'].plot(label="IBOV")
plt.legend()
plt.show()

profitability_wallet = valor_investido_norm['Total'].iloc[-1] - 1
profitability_ibov = ibov_norm['Adj Close'].iloc[-1] - 1

print(f"Wallet's profitability → {profitability_wallet:.1%}")
print(f"Ibov's profitability → {profitability_ibov:.1%}")