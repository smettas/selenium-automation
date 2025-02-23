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

driver.get("https://smallpdf.com/pdf-to-word")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@class='sc-8s01yt-4 dNifye']").send_keys("D:\sai files\sai passport.pdf")
input()