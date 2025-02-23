import time
import requests as requests

########## Driver Imports #########
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

########## Wait Imports #####
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

######### Exception Imports ##########
from selenium.common.exceptions import *

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window

links = driver.find_elements(By.TAG_NAME,"a")
print("Total number of links: ",len(links))

count=0
for link in links:
    url=link.get_attribute("href")
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        count +=1
        print(url,"The link is Broken link")
    else:
        print("The link is valid Link.......")
print("Total number of broken links: ", count)