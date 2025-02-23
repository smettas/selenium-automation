import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

########This class for select the drop down purpose##############
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

my_wait = WebDriverWait(driver, 10, poll_frequency=2)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
windowID = driver.current_window_handle
print("Parent window: ", windowID)

my_wait.until(EC.presence_of_element_located((By.LINK_TEXT,"OrangeHRM, Inc"))).click()
windowIDs = driver.window_handles
print("Child window: ", windowIDs)

driver.switch_to.window(windowID)
print("This is last current title: ", driver.title)

for winID in windowIDs:
    driver.switch_to.window(winID)
    print(driver.title , driver.current_window_handle) 