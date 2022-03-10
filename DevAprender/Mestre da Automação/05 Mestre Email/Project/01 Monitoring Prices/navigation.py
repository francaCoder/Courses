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
from selenium.webdriver.chrome.options import Options
import os
from send_email import ReadEmail


chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHORME_BIN")
path_chromedriver = os.environ.get("CHORMEDRIVER_PATH")

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://cursoautomacao.netlify.app/dinamico")
sleep(3)

def verify_changes():
    basic_plan_price = driver.find_element_by_xpath("//li[@id='BasicPlan']")
    sleep(2)
    # print(basic_plan_price.text)
    if basic_plan_price.text != 'R$ 9.99 / ano':
        message = f"The price was changed to {basic_plan_price.text}"
        # Send email
        email = ReadEmail(origin_email=os.environ.get("EMAIL_SENDER"), password_email=os.environ.get("PASSWORD_EMAIL"))
        contact_list = ["matheus__.silva@outlook.com"]
        email.content("The price on website was changed", "Matheus", contact_list, message)
        email.send_email()


    elif basic_plan_price.text == 'R$ 9.99 / ano':
        print("The price continued the same")


# schedule.every(2).minutes.do(verify_changes)
#
# while True:
#     schedule.run_pending()
#     sleep(1)

verify_changes()
