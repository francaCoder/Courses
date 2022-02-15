from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.binary_location = os.getcwd() + os.sep + 'chrome-win' + os.sep + 'chrome.exe'
chromedriver_path = os.getcwd() + os.sep + 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
driver.get("https://cursoautomacao.netlify.app/")

"""
chrome_options = Options()

arguments = [....]

for arg in arguments:
    chrome_options.add_argument(arg)
main arguments
--start maximized / Inicia maximizado
--lang-BR / Idioma
--incognito / Usar o modo anônimo
--window-size=800, 800 / Resolução da janela em largura e altura
--headless / Roda em segundo plano
--disable-notifications
--disable-gpu
"""