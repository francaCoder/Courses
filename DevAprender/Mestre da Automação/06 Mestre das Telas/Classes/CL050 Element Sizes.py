import PySimpleGUI as psg

psg.theme("Reddit")

layout = [
    [psg.Text("Name", size=(10, 1)), psg.Text("E-mail", size=(10, 1))], # characters → 10 = Horizontal 1 = Vertical
    [psg.Input(size=(10, 1)), psg.Input(size=(10, 1))],
    [psg.Text("Birthday", size=(26, 1)), psg.Text("Which website do you visit the most?", size=(30, 1))],
    [psg.Input(size=(30, 1)), psg.Input(size=(30, 1))],

]

window = psg.Window("My window", layout)
window.read()