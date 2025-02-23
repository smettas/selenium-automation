import time  ####### Importing time module to use sleep function

from selenium import webdriver  ######## Importing webdriver module from selenium
from selenium.webdriver.chrome.service import Service  ######## For setting up ChromeDriver service
from webdriver_manager.chrome import ChromeDriverManager  ######### Automatically manages ChromeDriver
from selenium.webdriver.common.by import By  ######## For locating elements using different strategies

from selenium.webdriver.support.select import Select  ####### For handling drop-down elements (though not used here)

from selenium.webdriver.support.ui import WebDriverWait  ###### To add explicit waits
from selenium.webdriver.support import expected_conditions as EC  ###### For waiting conditions like presence_of_element

from selenium.common.exceptions import *  ####### Importing all common exceptions

#ops = webdriver.ChromeOptions()
#ops.add_argument("--disable-notifications")
#driver = webdriver.Chrome(service=service, options=ops) 
                                # ........In 20th line we need to replace this line, to stop loction popup when newly opened tab  in asking

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.gps-coordinates.net/my-location")
driver.maximize_window()
time.sleep(10)
