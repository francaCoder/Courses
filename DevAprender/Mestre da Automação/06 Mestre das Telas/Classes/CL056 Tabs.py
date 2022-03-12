import PySimpleGUI as psg

tab1_register = [
    [psg.Text("Type your name:")],
    [psg.Input()],
    [psg.Text("Type your state")],
    [psg.Input()],
    [psg.Button("Save Register")],
]

tab2_velocity = [
    [psg.Text("Searches per day:")],
    [psg.Slider(range=(1, 10), default_value=1)],
    [psg.Button("Save Velocity")]
]

layout = [
    [psg.TabGroup([
        [psg.Tab("Register", tab1_register)],
        [psg.Tab("Velocity", tab2_velocity)]
    ])]
]

window = psg.Window("My window", layout)
window.read()