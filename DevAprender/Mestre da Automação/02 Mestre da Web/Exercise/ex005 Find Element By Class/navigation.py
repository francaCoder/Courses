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
        # nav_bar = self.driver.find_element_by_class_name("navbar")
        nav_bar = self.driver.find_element_by_class_name("navbar.navbar-expand-md.navbar-light")
        # Replace the black spaces to .

        # nav_bar = self.driver.find_element_by_class_name(str(input("Class: ")).replace(" ", "."))
        # "navbar navbar-expand-md navbar-light"
        # result = navbar.navbar-expand-md.navbar-light
        if nav_bar is not None:
            print("'nav bar' was found")
        else:
            print("'nav bar' not found")


course = AutomateCourse()
course.Start()