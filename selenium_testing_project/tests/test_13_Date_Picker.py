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

my_wait = WebDriverWait(driver,10,poll_frequency=2)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

year="2026"
month="March"
day="25"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
time.sleep(5)

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//a[@title='Next']").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text==day:
        date.click()
        break;

time.sleep(5)
driver.switch_to.default_content()