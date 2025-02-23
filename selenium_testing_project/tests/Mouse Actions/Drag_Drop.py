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

driver.get("http://www.dhtmlgoodies.com/packages/dhtml-suite-for-applications/demos/demo-drag-drop-3.html")
driver.maximize_window()

source_element=driver.find_element(By.XPATH,"//div[@id='box6']")
target_element=driver.find_element(By.XPATH,"//div[@id='box106']")

act=ActionChains(driver)
act.drag_and_drop(source_element,target_element).perform()

input()