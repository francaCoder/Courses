from pprint import pprint
import matplotlib.pyplot as plt
import requests
import json

# # Specific date
# quotes = requests.get("https://economia.awesomeapi.com.br/BTC-BRL/300?start_date=20211101&end_date=20220504")
#
# quotes_btc = quotes.json()
# # pprint(quotes_btc)
# list_quotes_btc = [item['bid'] for item in quotes_btc]
# list_quotes_btc.reverse()
# print(list_quotes_btc)
#
# # Graphic
#
# plt.figure(figsize=(15, 5))
# plt.plot(list_quotes_btc[50:100])
# plt.show()



# Requisição de data especifica

# Ano, mês, Dia
cotacoes = requests.get("https://economia.awesomeapi.com.br/BTC-BRL/200?start_date=20200101&end_date=20201031")

cotacoes_btc = cotacoes.json()

list_quotes_btc = [item['bid'] for item in cotacoes_btc]

print(list_quotes_btc)

plt.figure(figsize=(15, 5))
plt.plot(list_quotes_btc[50:100])

plt.show()
