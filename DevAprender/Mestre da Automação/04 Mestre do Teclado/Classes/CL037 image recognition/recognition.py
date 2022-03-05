import pyautogui

# Image on screen

print(pyautogui.locateOnScreen('file_name.jpg'))
# Coordinates

# center
center = pyautogui.locateCenterOnScreen('file_name.jpg')
# Or print this and then use the 'moveTo' and click.
pyautogui.click(center)