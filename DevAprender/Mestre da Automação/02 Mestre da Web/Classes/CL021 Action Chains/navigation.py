from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://cursoautomacao.netlify.com")

# Single Click
# chain = ActionChains(driver)
# button = driver.find_element_by_id("dropdownMenuButton")
# sleep(2)
# chain.click(button).perform()

# Command Sequence
# I need use a new chain
# sleep(2)
# chain2 = ActionChains(driver)
# radio_buttons = driver.find_element_by_xpath("//input[@id='WindowsRadioButton']")
#
# # Keyboard
# chain2.click(radio_buttons).pause(3).send_keys(Keys.ARROW_DOWN).pause(3).send_keys(Keys.ARROW_UP).perform()


# Right button
sleep(2)
chain3 = ActionChains(driver)

driver.execute_script("window.scrollBy(0, 400)")
sleep(2)
element = driver.find_element_by_id('botao-direito')
chain3.context_click(element).pause(1).send_keys(Keys.ARROW_DOWN*6).pause(1).click().perform()

# chain4 = chain3.context_click(element).pause(1)
# for c in range(6):
#     chain4.send_keys(Keys.ARROW_DOWN).perform()
#     sleep(0.5)
# chain4.click().perform()
