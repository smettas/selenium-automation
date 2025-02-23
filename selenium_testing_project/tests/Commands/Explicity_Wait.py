from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
#......driver.implicitly_wait(5) ...Implicity

my_wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
                                                                           ElementNotVisibleException,
                                                                           ElementNotSelectableException]) ###### We can use only Exception also

driver.get("https://opensource-demo.orangehrmlive.com")

#.....use this also in XPATH//a[normalize-space()='OrangeHRM, Inc']
#.....driver.find_element(By.XPATH,"//a[text()='OrangeHRM, Inc']").click() 
###### This is Explicity#########
search_link = my_wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='OrangeHRM, Inc']")))         #...No need find_element
search_link.click()
print("Full code is Executed sucessfully")