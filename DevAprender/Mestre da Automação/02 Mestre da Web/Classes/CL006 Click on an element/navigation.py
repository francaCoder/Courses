from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        button_menu = self.driver.find_element_by_id("dropdownMenuButton")
        button_menu.click()
        # JS code
        # self.driver.execute_script("arguments[0].click()",button_menu)
        # //section[@class="jumbotron"]/div/div[2]/div/div/a[3]



course = AutomateCourse()
course.Start()