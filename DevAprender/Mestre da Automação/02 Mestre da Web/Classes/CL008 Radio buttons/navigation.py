from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        button = self.driver.find_element_by_xpath("//section[@class='jumbotron']/div/div/div/input[@type='radio']")
        button.click()
        # if is_selected()...


course = AutomateCourse()
course.Start()