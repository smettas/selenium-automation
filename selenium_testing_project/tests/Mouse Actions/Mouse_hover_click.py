import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

########This class for select the drop down purpose##############
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

my_wait = WebDriverWait(driver, 10, poll_frequency=2)

driver.get("https://www.orangehrm.com/")
driver.maximize_window()

solutions=driver.find_element(By.XPATH,"//a[normalize-space()='Solutions']")
management=driver.find_element(By.XPATH,"//body/nav[contains(@class,'navbar navbar-expand-lg navbar-light fixed-top')]/div[contains(@class,'container-fluid')]/div[@id='navbarSupportedContent']/ul[contains(@class,'navbar-nav me-auto mb-2 mb-lg-0 web-menu')]/li[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]")
hr_admin=driver.find_element(By.XPATH,"//a[normalize-space()='HR Administration']")

act=ActionChains(driver)

act.move_to_element(solutions).move_to_element(management).move_to_element(hr_admin).click().perform()
time.sleep(5)
