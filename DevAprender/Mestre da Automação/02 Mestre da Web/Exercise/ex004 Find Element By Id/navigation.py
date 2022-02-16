from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
        # self.site = str(input("What's the site? "))
        # self.driver.get(self.site)


    def Start(self):
        # self.driver.get(str(input("Whats the site? ")))
        self.driver.get("https://cursoautomacao.netlify.app/")
        button_dropDown = self.driver.find_element_by_id("dropdownMenuButton")
        if button_dropDown is not None:
            print("drop down button found")
        else:
            print("'drop down' button not found")


course = AutomateCourse()
course.Start()