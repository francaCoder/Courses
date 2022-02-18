from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        sleep(2)
        challenges = self.driver.find_element_by_xpath("//a[text()='Desafios']")
        challenges.click()
        sleep(3)
        dropdown = self.driver.find_element_by_xpath("//section[6]//select[@id='paisesselect']")
        options = Select(dropdown)
        # Sequence: EUA, Africa, Chile
        options.select_by_index(2)
        sleep(3)
        options.select_by_index(4)
        sleep(3)
        options.select_by_index(6)
        sleep(3)


course = AutomateCourse()
course.Start()