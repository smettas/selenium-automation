import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
time.sleep(3)

fName = driver.find_element(By.XPATH,"//input[@id='FirstName']")
print("It is Displayed?: ",fName.is_displayed())
print("It is Enable?: ",fName.is_enabled())
time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"a.ico-login").click
print(driver.current_url)   
time.sleep(15)

driver.implicitly_wait(10)
