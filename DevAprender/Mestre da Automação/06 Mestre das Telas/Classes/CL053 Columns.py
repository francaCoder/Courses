import PySimpleGUI as psg

psg.theme("DarkGrey13")

left_column = [
    [psg.Text("User")],
    [psg.Input(key="User")],
    [psg.Text("Password")],
    [psg.Input(key="Password")],
]

middle_column = [
    [psg.Output(size=(40, 10))],
]

right_column = [
    [psg.Text("Which the website to automate?")],
    [psg.Checkbox("Option 1"), psg.Checkbox("Option 2"), psg.Checkbox("Option 3")],
]

layout = [
    [psg.Column(left_column), psg.Column(middle_column), psg.Column(right_column)]
]

window = psg.Window("Main Layout", layout)
window.read()
