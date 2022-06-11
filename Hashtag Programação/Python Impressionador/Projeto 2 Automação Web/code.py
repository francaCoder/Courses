import win32com.client as win32
import pandas as pd
from selenium import webdriver

products = pd.read_excel(r"teste_final.xlsx")

products.rename(columns={'Link Produto': 'Nome Produto'}, inplace=True)
products.fillna(0, inplace=True)

def tratar_texto(text):
    return float(str(text[3:]).replace(".", "").replace(",", "."))

#
# driver = webdriver.Chrome()
#
# print(products.info())
#
# disconto = 0.2
# enviar_email = False
#
# for i, line in products.iterrows():
#     # Amazon
#     driver.get(line['Amazon'])
#
#     price = driver.find_element_by_xpath("//*[@id='corePrice_feature_div']/div/span/span[2]/span[2]").text
#
#     price_amazon = str(price).replace(".", "") + "." + driver.find_element_by_xpath("//*[@id='corePrice_feature_div']/div/span/span[2]/span[3]").text
#
#     print(price_amazon)
#
#     # Lojas americanas
#     driver.get(line["Lojas Americanas"])
#
#     price_lame = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[3]/div[2]/div[1]/div[1]/div").text
#
#     price_lame = float(str(price_lame[3:]).replace(".", "").replace(",", "."))
#
#     # Magazine Luiza
#     driver.get(line["Magazine Luiza"])
#
#     price_mglu = driver.find_element_by_xpath("/html/body/div[1]/div/main/section[4]/div[4]/div/div/div/p[2]").text
#
#     price_mglu = float(str(price_mglu[3:]).replace(".", "").replace(",", "."))
#
#     original_price = line['Preço Original']
#
#     lista_precos = [
#         (price_amazon, "Amazon"),
#         (price_lame, "Lojas Americanas"),
#         (price_mglu, "Magazine Luiza"),
#         (original_price, "Preço Original")
#     ]
#
#     lista_precos.sort()
#
#     print(lista_precos)
#
#     products.loc[i, 'Preço Atual'] = lista_precos[0][0]
#     products.loc[i, 'Local'] = lista_precos[0][1]
#
#     products.to_excel("products.xlsx")
#
#     if lista_precos[0][0] <= original_price * (1-disconto):
#         enviar_email = True


# enviar_email = True
#
#
# if enviar_email:
outlook = win32.Dispatch("outlook.application")

email = outlook.CreateItem(0)

# informations
email.To = "matheusailvafds@gmail.com"
email.Subject = "Produto(s) com disconto"
email.Body = """
Salve França

Encontramos os seguintes produtos com desconto de 20%

Att,.
Python
"""

email.Send()
print("Finish")