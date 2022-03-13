import PySimpleGUI as psg

psg.theme("DarkGrey13")

# Create a function that returns a window for each window

# Window 1
def create_window1():
    layout = [
        [psg.Text("Register your name in the competition")],
        [psg.Button("Open the second window"), psg.Button("Exit")]
    ]
    return psg.Window("Window", layout, finalize=True)

def create_window2():
    layout = [
        [psg.Text("Welcome to the second window")],
        [psg.Ok()]
    ]
    return psg.Window("Window 2", layout, finalize=True)


window1, window2 = create_window1(), None

while True:
    window, event, values = psg.read_all_windows()
    if event in (psg.WIN_CLOSED, None):
        window.close()
        break
    if window == window1 and event == "Open the second window":
        window2 = create_window2()
    if window == window2 and event == "OK":
        print("'Ok' Button was pressed")