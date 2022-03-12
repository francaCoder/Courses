import PySimpleGUI as psg

layout_1 = [
    [psg.Text("Hello, we are in column 1")],
    [psg.Ok()]
]
layout_2 = [
    [psg.Text("Hello, we are in column 2")],
    [psg.Ok()]
]
layout_3 = [
    [psg.Text("Hello, we are in column 1")],
    [psg.Ok()]
]
layout_4 = [
    [psg.Text("Hello, we are in column 2")],
    [psg.Ok()]
]
layout_5 = [
    [psg.Text("Hello, we are in column 3")],
    [psg.Ok()]
]

main_layout = [
    [psg.Column(layout_1), psg.Column(layout_2)],
    [psg.Column(layout_3), psg.Column(layout_4), psg.Column(layout_5)],
]

window = psg.Window("My window", main_layout)
window.read()