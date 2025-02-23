import time  ####### Importing time module to use sleep function

from selenium import webdriver  ######## Importing webdriver module from selenium
from selenium.webdriver.chrome.service import Service  ######## For setting up ChromeDriver service
from webdriver_manager.chrome import ChromeDriverManager  ######### Automatically manages ChromeDriver
from selenium.webdriver.common.by import By  ######## For locating elements using different strategies

from selenium.webdriver.support.select import Select  ####### For handling drop-down elements (though not used here)

from selenium.webdriver.support.ui import WebDriverWait  ###### To add explicit waits
from selenium.webdriver.support import expected_conditions as EC  ###### For waiting conditions like presence_of_element

from selenium.common.exceptions import *  ####### Importing all common exceptions


######### Setting up ChromeDriver using the webdriver manager (automatically installs the driver)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

my_wait = WebDriverWait(driver, 10, poll_frequency=2)

####### Navigating to the target website
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

my_wait.until(EC.presence_of_element_located((By.ID,"Wikipedia1_wikipedia-search-input"))).send_keys("sai krishna")
driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
time.sleep(5)

lists = my_wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='wikipedia-search-result-link']/a")))
print("Total links founs: ", len(lists))

######## Iterate over each link found in the search results#########
for list in lists:
    list.click() ##### Click on each link
    time.sleep(2)

    handles = driver.window_handles    ########### Get all window handles after clicking the link

    driver.switch_to.window(handles[-1]) ######### Switch to the most recent window (new tab)
    print(f"This is current WindowID: {driver.current_window_handle}") ###### Printing current window handle
    print(f"This is the title for this Window: {driver.title}")  ##### Printing Title of the Window Page
    print()  ##### Empty line printing

    driver.close() ######## Closing the newly opened/current tab
    driver.switch_to.window(handles[0]) ######### Switch back to main window