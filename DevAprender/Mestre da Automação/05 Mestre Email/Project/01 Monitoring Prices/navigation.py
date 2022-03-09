"""
Understand the problem
I want to monitor the basic plan's price and when that changes, i need to be notified
1 - site → https://cursoautomacao.netlify.app/dinamico
2 - Selenium & PyautoGui
"""

import webbrowser
import pyautogui
import schedule
from time import sleep
from selenium import webdriver
import os



driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://cursoautomacao.netlify.app/dinamico")
sleep(3)

def verify_changes():
    basic_plan_price = driver.find_element_by_xpath("//li[@id='BasicPlan']")
    sleep(2)
    print(basic_plan_price.text)
    # if basic_plan_price.text != 'R$ 9.99 / ano':
    #     print(f"The price was changed to {basic_plan_price.text}")
    # elif basic_plan_price.text == 'R$ 9.99 / ano':
    #     print("The price continued the same")


# schedule.every(2).minutes.do(verify_changes())
#
# while True:
#     schedule.run_pending()
#     sleep(1)

