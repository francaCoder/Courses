# Masking the current IP
# Simulating that you are somewhere else around the world
# If you are blocked, you can use other IP
# If you want to enter a website a several times, you can use multiple IP's
# Some websites may block you for using different proxies

# 8.214.41.50
from time import sleep
from selenium import webdriver
import os

# PROXY = "8.214.41.50"

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--proxy-server={PROXY}")
webdriver_path = os.getcwd() + os.sep + "chromedriver.exe"

driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)
driver.get("https://www.myip.com")
sleep(100)