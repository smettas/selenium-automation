import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())   #Download chromedriver & install latestes version
driver = webdriver.Chrome(service=service)          #Open chrome Browser

driver.get("https://opensource-demo.orangehrmlive.com")       #Open OpenSource demo site
time.sleep(5)

driver.find_element(By.NAME,"username").send_keys("Admin")       #Find and enter username
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("admin123")      #Find and enter password
time.sleep(5)
driver.find_element(By.XPATH, "//button[@type='submit']").click()    #Find and click on submit
time.sleep(5)

actual_title = driver.title             #Getting title and stored in Actual_Title
expected_title = "OrangeHRM"            #Giving Value to Expected_Title
if actual_title==expected_title:        #Checking wether both Act and Exp is true or false
    print("Test is Passed")
else:
    print("test is Failed")

driver.close()                      #Closing driver browser
