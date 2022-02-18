# 4 - Check the checkboxes
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
        challenges = self.driver.find_element_by_xpath("//a[text()='Desafios']")
        challenges.click()
        sleep(3)
        check1 = self.driver.find_element_by_xpath("//input[@id='conversivelcheckbox']")
        check1.click()
        sleep(0.5)
        check2 = self.driver.find_element_by_xpath("//input[@id='offroadcheckbox']")
        check2.click()


course = AutomateCourse()
course.Start()