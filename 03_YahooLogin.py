from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path="C:\Bin/chromedriver.exe")
driver.get("https://login.yahoo.com/")
driver.find_element(by="name", value="username").send_keys("monikabobade@yahoo.in")
driver.find_element(by="name", value="signin").click()
time.sleep(2)
driver.find_element(by="name", value="password").send_keys("9403169928")
driver.find_element(by="name", value="verifyPassword").click()


# driver.find_element(by="class", value="missing-digit").send_keys("99")