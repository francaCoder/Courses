import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web

wallet = pd.read_excel("CarteiraMentoria.xlsx")
# web.DataReader()

print(wallet)

# Divisão da carteira em ativos

fig,(ax1, ax2) = plt.subplots(1, 2)

graphic1 = wallet['Valor Investido'].plot.pie(ax=ax1, labels=wallet['Ativos'], y=wallet['Valor Investido'], title="Distribuição de Ativos da Carteira", figsize=(15, 5), autopct="%.1f%%")
graphic1.set_ylabel('') # Remove the legend
plt.legend()


graphic2 = wallet.groupby('Tipo').sum().plot.pie(ax=ax2, y='Valor Investido', title="Classes de Ativos da Carteira", figsize=(15, 5), autopct="%.1f%%")
plt.show()

