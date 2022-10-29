from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://www.google.com/")
search_box = driver.find_element(by="name", value="q")
search_box.send_keys("Selenium")
time.sleep(3)
btn = driver.find_element(by="name", value="btnK")
btn.click()

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(3)

# driver.find_element_by_xpath (by="class", value="LC20lb MBeuO DKV0Md").click()
driver.find_element(By.CLASS_NAME, 'Selenium').click()
time.sleep(3)



# print(driver.page_source)
# print(driver.get_cookies())


