import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

########This class for select the drop down purpose##############
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.save_screenshot(os.getcwd()+"\\First_Screenshot.png")

regi_keys=Keys.CONTROL+Keys.RETURN
register=driver.find_element(By.XPATH,"//a[normalize-space()='Register']").send_keys(regi_keys)
tabs=driver.window_handles
driver.switch_to.window(tabs[1])
input()