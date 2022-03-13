import PySimpleGUI as psg

def create_window1():
    layout = [
        [psg.Text("Window 1")],
        [psg.Input()],
        [psg.Button("Next >"), psg.Button("Exit")],
    ]
    return psg.Window("Window 1", layout, finalize=True)

def create_window2():
    layout = [
        [psg.Text("Window 2")],
        [psg.Text("Which websites should be automated")],
        [psg.Checkbox("Site 1"), psg.Checkbox("Site 2")],
        [psg.Button("< Back"), psg.Button("Next >")],
    ]
    return psg.Window("Window 2", layout, finalize=True)

def create_window3():
    layout = [
        [psg.Text("Window 3")],
        [psg.Text("Receive completion notifications?")],
        [psg.Radio(
            "Yes", group_id="completion_notification"),
            psg.Radio("No", group_id="completion_notification")],
        [psg.Button("< Back"), psg.Button("Finalize settings")]
    ]
    return psg.Window("Window 3", layout, finalize=True)


window1, window2, window3 = create_window1(), None, None
while True:
    window, event, values = psg.read_all_windows()
    if window == window1 and event in (psg.WIN_CLOSED, "Exit"):
        window.close()
        break

    if window == window1:
        if event == "Next >":
            window.hide()
            window2 = create_window2()

    if window == window2:
        if event == "Next >":
            window2.hide()
            window3 = create_window3()
        elif event in (psg.WIN_CLOSED, "< Back"):
            window2.close()
            window1.un_hide()

    if window == window3 and event == "Finalize settings":
        window1.close()
        window2.close()
        window.close()
        break

    if window == window3 and event == "< Back":
        window3.hide()
        window2.un_hide()