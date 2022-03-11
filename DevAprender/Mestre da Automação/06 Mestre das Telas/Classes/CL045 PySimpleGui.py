import PySimpleGUI as psg

# theme
psg.theme("Reddit")

# Layout
layout = [
    [psg.Text("Type a Number: ")],
    [psg.Input()],
    [psg.OK()],
]

# Window

window = psg.Window("My Window", layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == "OK":
        print(values)
window.close()