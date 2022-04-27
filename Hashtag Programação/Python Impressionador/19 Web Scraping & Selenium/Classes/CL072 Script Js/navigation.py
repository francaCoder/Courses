from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver

# Open
driver = webdriver.Chrome()

driver.get("https://www.youtube.com")

WebDriverWait(driver, 30).until(EC.presence_of_element_located(
    (By.XPATH, "//input[@id='search']")
))

driver.find_element_by_xpath("//input[@id='search']").send_keys("python")
driver.find_element_by_xpath("//input[@id='search']").send_keys(Keys.ENTER)

sleep(2)
# Scroll
for c in range(20):
    scroll = 10000 * c
    driver.execute_script(f"window.scroll(0, {scroll})")
    sleep(1)

sleep(2)
videos = driver.find_elements_by_xpath("//a[@id='thumbnail']")

for video in videos:
    print(video.get_attribute("href"))
