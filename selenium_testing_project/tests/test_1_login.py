import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(5)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
time.sleep(5)

driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")
time.sleep(5)

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

actual_title = driver.title
expected_title = "Dashboard / nopCommerce administration"
if actual_title==expected_title:
    print("The test is Passed")
else:
    print("The Test is Failed")

driver.close()