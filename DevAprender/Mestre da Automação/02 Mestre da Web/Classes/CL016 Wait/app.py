"""
Looks like sleep
but the sleep's value is fixed.
- driver.implicitly_wait(seconds) can do action before last second different to 'sleep'. After time runs out it returns the Error.
- driver.explicitly_wait
"""

# explicitly
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *

self.wait = WebDriverWait(self.driver, 10, 1, [NoSuchElementException], [ElementNotVisibleException], [ElementNotSelectableException])
# driver, seconds, search attempts, ignore error



element = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "....")))
element.click()
# .visibility_of_element_located
# .visibility_of_all_element_located
