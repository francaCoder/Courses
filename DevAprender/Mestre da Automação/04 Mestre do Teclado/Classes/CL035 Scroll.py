import pyautogui
from time import sleep

pyautogui.moveTo(x=1500, y=500, duration=1)
sleep(1)
pyautogui.scroll(-150)
sleep(2)
pyautogui.scroll(150)


"""
< 0 = Down
> 0 = Up
"""