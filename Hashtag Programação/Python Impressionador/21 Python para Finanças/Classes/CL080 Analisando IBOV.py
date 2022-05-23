import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web

ibov_quote = web.DataReader('^BVSP', data_source='yahoo', start='2020-01-01', end='2020-11-10')
print(ibov_quote)

# 1
ibov_quote['Adj Close'].plot(figsize=(15, 5))


# 2 - BVSP return
bvsp_return = ibov_quote['Adj Close'][-1] / ibov_quote['Adj Close'][0] -1
print(f"{bvsp_return:.2%}")

# Moving Average
ibov_quote['Adj Close'].plot(figsize=(15, 5), label="IBOV")
ibov_quote['Adj Close'].rolling(21).mean().plot(label="A.M21")
ibov_quote['Adj Close'].rolling(34).mean().plot(label="A.M34")

plt.legend()
plt.show()
