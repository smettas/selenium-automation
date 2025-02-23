import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.flipkart.com/")
driver.find_element(By.NAME, "q").send_keys("mobies")
time.sleep(3)

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)