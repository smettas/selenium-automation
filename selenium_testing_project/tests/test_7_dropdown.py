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

driver.get("https://www.opencart.com/?route=account/register")
driver.maximize_window()

drop_country_element = driver.find_element(By.XPATH,"//select[@id='input-country']")
drop_options = Select(drop_country_element)

##### SElecting the India option from drop down #########
drop_options.select_by_visible_text("India")
time.sleep(3)

####To list or display all Elements in a drop down
all_options = drop_options.options

for opt in all_options:
    print(opt.text)

print("Total number of options in drop down: ",len(all_options))