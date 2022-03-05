import pyautogui
from mouseinfo import mouseInfo

# print(mouseInfo())


for c in range(6):
    pyautogui.moveTo(x=1209, y=232, duration=1)
    pyautogui.dragTo(x=1795, y=795, duration=1)