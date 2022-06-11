import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web


# tem que passar o ticker da moeda que você quer pegar
# data_source - da onde ele vai pegar
# start & end

cotacao_ibov = web.DataReader("^BVSP", data_source="yahoo", start="2020-01-01", end="2020-11-10")

print(cotacao_ibov.info())

# Matplotlib
cotacao_ibov['Adj Close'].plot(figsize=(15, 5))

plt.show()

# Qual foi o retorno do IBOV?
# A última cotação, dividida pela primeira - 1

retorno_ibov = cotacao_ibov['Adj Close'][-1] / cotacao_ibov['Adj Close'][0] - 1

print(f"{retorno_ibov:.1%}")


# média móvel

cotacao_ibov['Adj Close'].plot(figsize=(15, 5), label="IBOV")
cotacao_ibov['Adj Close'].rolling(21).mean().plot(label="MM21") # Média (mean) de 21 dias de uma janela rolante (rolling)

# Acrescentar uma média móvel
cotacao_ibov['Adj Close'].rolling(34).mean().plot(label="MM34") # Média (mean) de 21 dias de uma janela rolante (rolling)


plt.legend() # Precisa colocar esse pra ir a legenda
plt.show()