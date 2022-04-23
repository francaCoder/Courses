# Robot process automation - RPA
from time import sleep
import pyautogui as py
import pandas as pd
import pyperclip

# print(py.KEYBOARD_KEYS)

# """
# pyautogui.write
# pyautogui.click
# pyautogui.LocateOnScreen
# pyautogui.hotkey
# pyautogui.press
# """

# Press windows
# Type "Chrome"
# Press Enter

py.alert("O códido vai começar, não mexa em nada enquanto o código estiver rodando, quando terminar eu te aviso.")
py.PAUSE = 1.5

# Open Chrome
py.press('win')
py.write('Chrome')
py.press('enter')

# Gmail
py.write('Gmail')
py.press('enter')

x, y, width, height = py.locateOnScreen('search_google.png')
py.click(x + width/2, y + height/2)

while not py.locateOnScreen('field_write.png'):
    sleep(1)

sleep(1)

x, y, width, height = py.locateOnScreen('menu.png')
py.click(x + width/2, y + height/2)

x, y, width, height = py.locateOnScreen('contacts.png')
py.click(x + width/2, y + height/2)


while not py.locateOnScreen('wait_contacts.png'):
    sleep(1)

sleep(1)

x, y, width, height = py.locateOnScreen('export.png')
py.click(x + width/2, y + height/2)

x, y, width, height = py.locateOnScreen('export_confirm.png')
py.click(x + width/2, y + height/2)

py.hotkey('ctrl', 'pgup')

while not py.locateOnScreen('field_write.png'):
    sleep(1)

x, y, width, height = py.locateOnScreen('field_write.png')
py.click(x + width/2, y + height/2)

py.write("Matheus")
py.press('enter')
py.press("tab")

py.write("Pagamento")
py.press('enter')
py.press("tab")

text = """
Salve exemplo,

Para de atrasar os pagamentos e manda o dinheiro aí

abs e tmj
"""

pyperclip.copy(text)
py.hotkey('ctrl', 'v')