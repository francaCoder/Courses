import pyautogui
from mouseinfo import mouseInfo
"""
Parameters
x / y → Localization
clicks → How many clicks
interval → Looks sleep
Button → PRIMARY / SECONDARY
Duration
"""

# print(mouseInfo())

pyautogui.click(x=1200, y=772, clicks=100, interval=1, button="left", duration=2)

pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.leftClick()
pyautogui.middleClick()
pyautogui.tripleClick()