from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--lang=pt-BR")
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")

    def start(self):
        self.driver.get("https://www.cursoautomacao.netlify.app/")


course = AutomateCourse()
course.start()
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
#
# chrome_options = Options()
# chrome_options.binary_location = os.getcwd() + os.sep + 'chrome-win' + os.sep + 'chrome.exe'
# chromedriver_path = os.getcwd() + os.sep + 'chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
# driver.get("https://cursoautomacao.netlify.app/")