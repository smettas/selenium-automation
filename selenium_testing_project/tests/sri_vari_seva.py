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
my_wait = WebDriverWait(driver, 10, poll_frequency=2)

driver.get("https://srivariseva.tirumala.org/#/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@placeholder='Mobile Number']").send_keys("7032022441")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("9705533495@Sai")
time.sleep(5)

enter_link = my_wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Login']")))
enter_link.click()

my_wait.until(EC.presence_of_element_located((By.CLASS_NAME,"mat-list-item-content"))).click()

driver.find_element(By.XPATH,"//input[@name='firstNm']").send_keys("SaiMass")
time.sleep(5)