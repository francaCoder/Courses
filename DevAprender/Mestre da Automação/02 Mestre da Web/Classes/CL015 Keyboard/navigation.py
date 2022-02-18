from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        sleep(2)
        windows_button = self.driver.find_element_by_xpath(
            "//input[@id='WindowsRadioButton']")
        windows_button.click()
        sleep(1)
        windows_button.send_keys(Keys.ARROW_DOWN) # Or Keys.DOWN
        # Keys.TAB  -  Next element


course = AutomateCourse()
course.Start()