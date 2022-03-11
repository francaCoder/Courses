import PySimpleGUI as psg
import sys
from time import sleep

# psg.popup("Hello, are you logged", custom_text=("Continue", "Exit"))
# file_path = psg.popup_get_file("Choose a file")

# answer = psg.popup_yes_no(
#     "Are you ready to see how to create pop-ups using PySimpleGUI?", "Are you ready?"
# )
#
# if answer == "No":
#     psg.popup_cancel("Well...Let's close the program.")
#     sys.exit()
#
# psg.popup_non_blocking("Your answer was:", answer, location=(1000, 600)) # X - Y

text = psg.popup_get_text("This is a PopUp to get a text", location=(1000, 200))

psg.popup_get_file("")
psg.popup_get_folder("")
psg.popup()
psg.popup_no_titlebar()
psg.popup_no_border()
psg.popup_no_frame()
psg.popup_ok_cancel()

for c in range(10):
    psg.popup_no_wait("Don't block", location=(500+100*c, 500))
psg.popup_auto_close("PopUp auto-close", auto_close=True, auto_close_duration=5)