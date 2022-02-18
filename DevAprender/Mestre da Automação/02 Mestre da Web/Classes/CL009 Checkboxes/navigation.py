from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        checkbox = self.driver.find_element_by_id("//section[@class='jumbotron'][2]/div/div/div/input[@class='form-check-input']")
        checkbox.click()


course = AutomateCourse()
course.Start()