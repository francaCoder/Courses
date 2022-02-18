# 2 - Enter your name in the field below

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
        data_field = self.driver.find_element_by_xpath("//section[@class='jumbotron desafios2']/input[@id='dadosusuario']")
        # data_field = self.driver.find_element_by_xpath("//section[@class='jumbotron desafios2']/input[@class='form-control']")
        # data_field = self.driver.find_element_by_xpath("//section[@class='jumbotron desafios2']/input")
        data_field.click()
        data_field.send_keys("Matheus França")


course = AutomateCourse()
course.Start()