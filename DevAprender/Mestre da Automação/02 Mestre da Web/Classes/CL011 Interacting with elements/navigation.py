from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        checkbox_list = self.driver.find_elements_by_xpath("//input[@type='checkbox']")
        # clicks = 0
        for checkbox in checkbox_list:
            checkbox.click()
            # clicks += 1
            # if clicks >= 3:
            #     break



course = AutomateCourse()
course.Start()