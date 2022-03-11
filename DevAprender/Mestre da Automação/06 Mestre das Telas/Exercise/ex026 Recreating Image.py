import PySimpleGUI as psg

psg.theme("Reddit")

layout = [
    [psg.Text("Type your name:")],
    [psg.Input()],
    [psg.Text("Type your age:")],
    [psg.Input()],
    [psg.OK()],
]

window = psg.Window("My Window", layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        window.close()
        break
    if event == "OK":
        print(values)
