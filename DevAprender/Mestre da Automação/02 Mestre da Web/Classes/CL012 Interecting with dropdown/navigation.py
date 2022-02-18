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
        dropdown = self.driver.find_element_by_xpath("//select[@id='paisselect']")
        options = Select(dropdown)
        options.select_by_index(2)
        sleep(3)
        options.select_by_index(1)
        sleep(3)
        options.select_by_index(0)

        # options.select_by_value("brasil", "estadosunidos", "canada")
        # options.select_by_visible_text("Brasil", "Estados Unidos", "Canada")


course = AutomateCourse()
course.Start()