import mouseinfo
import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# print(mouseinfo.mouseInfo())

chrome_options = Options()
chrome_options.add_argument('--lang=pt-BR')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)

driver.get("https://lagged.com.br/jogo/1143/#goog_slotcar_ad")
sleep(3)

pyautogui.moveTo(x=509, y=474, duration=1)
pyautogui.click()
# Play

pyautogui.moveTo(x=253, y=300, duration=2)
# Dog
while True:
    for c in range(1, 50):
        pyautogui.click()

    # Upgrades
    pyautogui.moveTo(x=581, y=240, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(x=253, y=300, duration=0.5)
    pyautogui.click()