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

######## Pixel Value #######
pixels=driver.execute_script("return window.pageYOffset;")
print(pixels)

########### Scroll down page by pixels ########
driver.execute_script("window.scrollBy(0,2000)","")
input()

########### Scroll down page till end ##########
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  ###(for reverse bottom to top[0,-document.body....]) use minus symbol
input()

########## Scroll down the page still element is visible #########
element=driver.find_element(By.XPATH,"//h2[normalize-space()='Talent Management']")
driver.execute_script("arguments[0].scrollIntoView();", element)
input()

