from selenium import webdriver
import PySimpleGUI as psg
import threading

psg.theme("DarkGrey13")

LICENSES = ["H1H124-H1H124-H1H124-H1H124", "1D2D1-1D2D1-1D2D1-1D2D1"]

def create_window1():
    layout = [
        [psg.Text("Type your product's license:"), psg.Input(key="License")],
        [psg.Button("Validate"), psg.Button("Exit"), psg.Text(key="Approval_status", size=(30, 1))]
    ]

    return psg.Window("First Window", layout, finalize=True)


def create_window2():
    layout = [
        [psg.Text("Which task dou you like to automate?")],
        [psg.Button("Verify Prices")]
    ]
    return psg.Window("Welcome to my Program!", layout, finalize=True)


def extract_prices(tab):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://cursoautomacao.netlify.app/produtos1.html")
    products_price = driver.find_element_by_xpath("//p[@class='price-container']")

    prices_list = []

    for value in products_price:
        prices_list.append(value.text)
    driver.quit()

    tab.write_event_value("Automation_Finished", prices_list)


window1, window2 = create_window1(), None
thread_web = None

while True:
    window, event, values = psg.read_all_windows()
    if event == psg.WIN_CLOSED or event == "Exit":
        if window == window1:
            window1.close()
            break
        if window == window2:
            window1.close()
            window2.close()
            break

    elif event == "Validate":
        if values['License'] in LICENSES:
            window1.close()
            window2 = create_window2()
        else:
            window1['Approval_status'].update("Invalid License")

    elif event == "Verify Prices" and thread_web == None:
        thread_web = threading.Thread(target=extract_prices, args=(window,), daemon=True)
        thread_web.start()

    elif event == "Automation_Finished":
        thread_web.join()
        thread_web = None
        prices = values['Automation_Finished']
        for price in prices:
            psg.popup_ok(price)

window.close()

