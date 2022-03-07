import pyautogui
from mouseinfo import mouseInfo



# print(mouseInfo())
# Png or Jpg
image = pyautogui.screenshot("tela1.jpg")

# Or

image = pyautogui.screenshot("tela2", region=(737, 302, (1205-737), (416-302)))