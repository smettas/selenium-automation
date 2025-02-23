import time
import requests as requests

########## Driver Imports #########
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

########## Wait Imports #####
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

######### Exception Imports ##########
from selenium.common.exceptions import *


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

my_wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=(NoSuchElementException,ElementNotVisibleException))

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

check_box = my_wait.until(EC.presence_of_all_elements_located((By.XPATH,"//input[@name='profession' and @type='checkbox'] | //input[@name='tool' and @type='checkbox']")))
for i in range(len(check_box)):
    check_box[i].click()
    print("Check boxes are selected")
print("All code is executed")
time.sleep(20)
driver.quit()