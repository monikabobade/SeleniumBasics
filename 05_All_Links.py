from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.find_elements(by="TagName", value="a")


