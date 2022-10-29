from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path="C:\Bin/chromedriver.exe")
driver.get("http://cookbook.seleniumacademy.com/Config.html")
# for checkbox
# if not
driver.find_element(by="name", value="airbags").click()
time.sleep(2)

# for radio button
driver.find_element(by="name", value="fuel_type").click()
time.sleep(2)
driver.find_elements(by="name", value="fuel_type")[1].click()