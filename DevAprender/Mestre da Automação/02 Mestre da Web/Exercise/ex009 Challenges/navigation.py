"""
# CHALLENGES!!

1 - Find 1 element result with "Parágrafo" text
2 - Find 4 elements results with "Dropdown" or "Clássico" text
3 - Find 1 element result with "Elementos" and "Botões" text
4 - Find 1 element result with "Exemplo abrir Nova Janela" text
5 - Find the element with "divBotao" id
6 - Find 4 elements results with "form-control" class
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)

    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        #1
        paragraph = self.driver.find_element_by_xpath("//*[text()='Parágrafo']")
        paragraph = self.driver.find_element_by_xpath("//*[contains(text(), 'Parágrafo')]")
        paragraph = self.driver.find_element_by_xpath("//section[@class='jumbotron'][2]//div//div[4]/h4[text()='Parágrafo']")
        paragraph = self.driver.find_element_by_xpath("//*[starts-with(text(), 'Parágrafo')]")

        if paragraph is not None:
            print("'paragraph' were found")
        elif paragraph is None:
            print("'paragraph' not found")

        #2
        dropdown = self.driver.find_element_by_xpath("//*[contains(text(), 'Dropdown') or contains(text(), 'Clássico')]")

        if dropdown is not None:
            print("'paragraph' were found")
        elif dropdown is None:
            print("'paragraph' not found")

        # 3
        elements = self.driver.find_element_by_xpath("//*[contains(text(), 'Elementos') and contains(text(), 'botões'))]")

        # 4
        new_window = self.driver.find_element_by_xpath("//section[@class='jumbotron'][3]/div/div/h4[contains(text(), 'Exemplo abrir Nova Janela')]")

        # 5
        button = self.driver.find_element_by_id("divBotao")

        if button is not None:
            print("'button' was found")
        elif button is None:
            print("'button' not found")

        #6
        form = self.driver.find_element_by_class_name("form-control")
        if form is not None:
            print("'form' was found")
        elif form is None:
            print("'form' not found")


course = AutomateCourse()
course.Start()