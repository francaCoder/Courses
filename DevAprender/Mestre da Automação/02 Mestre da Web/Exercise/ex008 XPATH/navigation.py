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
        # //tag[@atributo="valor"]
        buttons = self.driver.find_element_by_xpath("//*[contains(text(), 'Exemplo')]")
        # //* - generic
        # //*[contains(text(), 'Exemplo')]
        # // *[contains(text(), 'Exemplo') or contains(text(), 'Dropdown')]
        # // *[contains(text(), 'Exemplo') and contains(text(), 'Checkbox')]
        # Starts from:
        # //*[starts-with(text(), "Elementos")]
        # //*[starts-with(@class, "btn")]
        # find by text
        # //*[text()="Dropdown Clássico"]
        # ID
        #//button[@id="dropdownMenuButton"]
        # or
        #//section[@class="jumbotron"]
        #//thead[@class="thead-dark"]//th[3]


        if buttons is not None:
            print("'Buttons' were found")
        else:
            print("'Buttons' not found")


course = AutomateCourse()
course.Start()