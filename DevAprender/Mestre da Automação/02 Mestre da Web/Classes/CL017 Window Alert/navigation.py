from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        sleep(2)
        self.driver.execute_script("scroll(0,850)")
        sleep(3.5)
        name = self.driver.find_element_by_xpath("//input[@id='nome']")
        name.click()
        name.send_keys("Matheus")
        sleep(2)
        # Alert
        # alert = self.driver.find_element_by_xpath("//input[@id='buttonalerta']")
        # alert.click()
        # sleep(1)
        # alert1 = self.driver.switch_to.alert
        # alert1.accept()

        # Confirm(type submit) or Prompt:
        sleep(2)
        confirm = self.driver.find_element_by_xpath("//input[@id='buttonconfirmar']")
        confirm.click()
        sleep(1)
        confirm1 = self.driver.switch_to.alert
        confirm1.accept()
        # Or → confirm1.dismiss()

        # Prompt


course = AutomateCourse()
course.Start()