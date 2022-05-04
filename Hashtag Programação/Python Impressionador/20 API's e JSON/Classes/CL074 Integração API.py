from pprint import pprint

import requests
import json

quotes = requests.get("https://economia.awesomeapi.com.br/json/all")
print(quotes)
# 200 = OK

quotes_dic = quotes.json()
pprint(quotes_dic)