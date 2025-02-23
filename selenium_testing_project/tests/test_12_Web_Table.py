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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1.Count Number of rows and coumns?????????????
rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
columns = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")

print(f"The total rows are: {len(rows)}") ####Number of Rows
print(f"The total columns are: {len(columns)}")  #####Number of Columns
print()

#2.Read Specific row and column data??????? 
specific_data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[4]/td[2]")
print(specific_data.text)
print()

#3.Read all Rows and Columns data???????...... Use for&Nested for loop
# for r in range(2,len(rows)+1):
#     for c in range(1,len(columns)+1):
#         data = my_wait.until(EC.presence_of_element_located((By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[{c}]"))).text  
#         print(data) ### To get data side by side for each every iteration use end keyword........print(data.text, end=" ")
#     print()

#4.Read data based on Condition??????
#i want book names whose author is Mukesh.......condition
book_name = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody//td[1]")
author = driver.find_elements(By.XPATH,"table[@name='BookTable']/tbody//td[2]")

for b in range(len(book_name)+1):
    a_name = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{b}]/td[2]").text 
    if a_name=="Mukesh":
        b_name = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{b}]/td[2]").text 
        print(b_name,a_name)
print()
