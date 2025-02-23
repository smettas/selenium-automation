import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains

########This class for select the drop down purpose##############
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

my_wait = WebDriverWait(driver,10,poll_frequency=2)

driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("This is sai krishna metta")

act=ActionChains(driver)

#####In a Multi line code######
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()


### In a single line code#######
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() #Selecting text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() #Copying text

act.send_keys(Keys.TAB).perform() #Clicking on TAB

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() #Pasting the text

input()
