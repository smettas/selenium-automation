import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

location=os.getcwd()

def chrome_setup():
    service=Service(ChromeDriverManager().install())
    preferences={"download.default-directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    ops.add_argument("--disable-notifications")
    driver=webdriver.Chrome(service=service,options=ops)
    return driver

driver=chrome_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
#driver.save_screenshot("filename.png") 
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
input()