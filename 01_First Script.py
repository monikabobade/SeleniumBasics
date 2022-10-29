from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# import time
#driver=webdriver.Chrome(executable_path="C:\Bin/chromedriver.exe")
# driver =webdriver.Chrome()
#driver=webdriver.Chrome(executable_path="Resources\chromedriver.exe")
#driver=webdriver.Chrome(executable_path="")
# driver.get("https://www.google.com/")
# title = driver.title
# print(title)
# assert driver.title == "Google", "Page Title Did not Match"
# # time.sleep(5)
# driver.close()


# ---------------------------------------
# driver = webdriver.Edge("Resources/msedgedriver.exe")
# driver.get("https://www.google.com/")
# driver.minimize_window()
# # time.sleep(5)
# # driver.close()
# --------------------------------------------
# options = Options()
# options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path="../Resources/geckodriver.exe")
# driver = webdriver.Firefox()
driver.get("https://www.google.com/")

