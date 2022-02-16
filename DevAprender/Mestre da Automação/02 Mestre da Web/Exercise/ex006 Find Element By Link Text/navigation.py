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
        # link = self.driver.find_element_by_link_text("Desafios")
        link = self.driver.find_element_by_partial_link_text("fios")

        if link is not None:
            print("'Link' was found")
        else:
            print("'Link' not found")


course = AutomateCourse()
course.Start()