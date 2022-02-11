# 1 - Create a webdriver browser
# 2 - Navigate to a website
# 3 - Find elements
# 4 - Interact with them by typing or clicking

from selenium import webdriver


# 1
driver = webdriver.Chrome(executable_path="chromedriver.exe")

# 2
driver.get("https://automatize.netlify.app/")

# 3 (Press F12 and Look for some unique feature of the element you want to select)
email_field = driver.find_element_by_id("email")

# 4
# Click
email_field.click()
# Type
email_field.send_keys("matheus@outlook.com")

password_field = driver.find_element_by_id("senha")
password_field.click()
password_field.send_keys("123456789")

button_field = driver.find_element_by_xpath("//button[text()='Enviar']")
button_field.click()