import PySimpleGUI as psg

psg.theme("Reddit")

layout = [
    [psg.Text("Type the message:")],
    [psg.Multiline(size=(50, 10))],
]

window = psg.Window("Multiline", layout)
window.read()