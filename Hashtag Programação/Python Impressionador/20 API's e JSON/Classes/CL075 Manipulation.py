from pprint import pprint
import matplotlib.pyplot as plt
import requests
import json

quotes = requests.get("https://economia.awesomeapi.com.br/json/all")
print(quotes)
# 200 = OK

quotes_dic = quotes.json()
pprint(quotes_dic)

# What was the last dollar's quote?

print(quotes_dic['USD']['bid'])
print(quotes_dic['EUR']['bid'])
print(quotes_dic['BTC']['bid'])

last_days = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/30")

quotes_days_dic = last_days.json()

# for day in quotes_days_dic:
#     print(day['bid'])

list_dollar_quotes = [day['bid'] for day in quotes_days_dic]
print(list_dollar_quotes)
