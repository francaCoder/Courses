import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

carteira = pd.read_excel("CarteiraMentoria.xlsx")

# # Vamos ver a divisão da carteira em ativos
# # Quero um gráfico de pizza
#
# # carteira['Valor Investido'].plot()
#
# # Plotar 2 gráficos lado a lado
# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.set_size_inches(15, 5)
#
# grafico1 = carteira.plot.pie(ax=ax1, labels=carteira['Ativos'], y='Valor Investido', legend=False, title="Distribiução de Ativos da Carteira", autopct="%.1f%%") # pie = pizza
# # labels é o nome dos valores do eixo x no gráfico de pizza, que colocaremos o nome de cada ativo e no eixo Y colocaremos o valor investido de cada um
# grafico1.set_ylabel("")
#
# # legend=False - desativar a legenda
# # title - título do gráfico
#
# grafico2 = carteira.groupby('Tipo').sum().plot.pie(ax=ax2, y='Valor Investido', legend=False, title="Distribiução de Ativos da Carteira", autopct="%.1f%%")
# grafico2.set_ylabel("")
#
#
# plt.show()


# Pegando cotações da internet


# Ibovespa
ibov_df = web.DataReader("^BVSP", data_source='yahoo', start="2022-01-01", end='2022-06-10')
print(ibov_df.info())

ibov_df['Adj Close'].plot(figsize=(15, 5))



carteira_df = pd.DataFrame()

for ativo in carteira['Ativos']:
    if ativo != "Tesouro Selic":
        try:
            carteira_df[ativo] = web.DataReader(f"{ativo}.SA", data_source='yahoo', start="2022-01-01", end='2022-06-10')['Adj Close']
        except:
            continue

print(carteira_df)
print(carteira_df.info())

link = "https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv"

tesouro_df = pd.read_csv(link, sep=";", decimal=",")

tesouro_df['Data Base'] = pd.to_datetime(tesouro_df['Data Base'], format="%d/%m/%Y") # Transforma a coluna em um datetime, colocando o parâmetro format avisando qual é o formato da data na nossa tabela pra ele entender e transformar

tesouro_df = tesouro_df.loc[tesouro_df['Tipo Titulo'] == "Tesouro Selic", :]

# Agora temos que juntar o tesouro selic com a carteira

# Colocando uma coluna que tem o mesmo nome de alguma coluna que a nossa tabela da carteira
tesouro_df.rename(columns={'Data Base': 'Date'}, inplace=True)

carteira_df = carteira_df.merge(tesouro_df[['Date', 'PU Base Manha']], on='Date', how='left')


carteira_df.rename(columns={'PU Base Manha': 'Tesouro Selic'}, inplace=True)
carteira_df.ffill(inplace=True)

print(carteira_df.info())

# Calcular o valor investido

valor_investido = carteira_df.copy()

for i, ativo in enumerate(carteira['Ativos']):
    try:
        # valor_investido[ativo] = valor_investido[ativo] * carteira['Qtde'][i]
        valor_investido[ativo] = carteira_df[ativo] * carteira.loc[carteira['Ativos'] == ativo, 'Qtde'].values[0]
    except:
        continue

valor_investido.set_index('Date', inplace=True)
valor_investido['Total'] = valor_investido.sum(axis=1) # eixo linha


valor_investido_norm = valor_investido / valor_investido.iloc[0]
ibov_df_norm = ibov_df / ibov_df.iloc[0]


valor_investido_norm['Total'].plot(figsize=(15, 5), label="Carteira")
ibov_df_norm['Adj Close'].plot(label='IBOV')


plt.legend()
plt.show()