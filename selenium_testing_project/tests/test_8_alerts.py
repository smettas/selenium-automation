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

driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()   ###[normalize-space()] is equals to text()
time.sleep(5)

####### creating variable for swith alert driver instance
my_alert = driver.switch_to.alert

print(my_alert.text)  ####Printing TEXT which is available in the alert
my_alert.send_keys("Hey Sai!") #####passing the text in box
my_alert.accept()  #### clicking OK in alert
#my_alert.dismiss()  #### clicking CANCEL in alert

######This is for result means, in web page we will see this#####
result = driver.find_element(By.XPATH,"//p[@id='result']")
print(result.text)