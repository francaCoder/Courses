from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        # Common methods
        self.driver.get("https://cursoautomacao.netlify.app/") # navigation
        self.driver.maximize_window()
        self.driver.refresh() or self.driver.get(self.driver.current_url)
        self.driver.page_source() # Page's code
        self.driver.close() # Close the current window
        self.driver.quit() # Close all tabs
        self.driver.back() # Back one page
        self.driver.forward() # Advance one page
        self.driver.title() # Page's title


course = AutomateCourse()
course.Start()