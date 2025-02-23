import time
import XLUtils

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.maximize_window()

file="D:\\Sai Work\\Python\\Practice\\simple interest.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    ######## Reading data from Excel #######
    principle=XLUtils.readData(file,"Sheet1",r,1)
    annualRate=XLUtils.readData(file,"Sheet1",r,2)
    periodUnit=XLUtils.readData(file,"Sheet1",r,3)
    periodValue=XLUtils.readData(file,"Sheet1",r,4)
    expectedValue=XLUtils.readData(file,"Sheet1",r,5)

    ######### Passing data to the Application #######
    driver.find_element(By.XPATH,"//input[@id='principleAmount']").clear()
    driver.find_element(By.XPATH,"//input[@id='principleAmount']").send_keys(principle)

    driver.find_element(By.XPATH,"//input[@id='annualrate']").clear()
    driver.find_element(By.XPATH,"//input[@id='annualrate']").send_keys(annualRate)

    period=Select(driver.find_element(By.XPATH,"//select[@id='periodUnit']"))
    period.select_by_visible_text(periodUnit)

    driver.find_element(By.XPATH,"//input[@id='periodInDigit']").clear()
    driver.find_element(By.XPATH,"//input[@id='periodInDigit']").send_keys(periodValue)
    
    actualValue=driver.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div[2]/div[1]/div[2]/div/div[4]/div/div/div[2]/span[2]").text
    actualValue=actualValue.replace("₹","").replace(",","").strip()
    ######## Validation ########
    if float(expectedValue)==float(actualValue):
        print("Passed")
        XLUtils.writeData(file,"Sheet1",r,7,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,7)
    else:
        print("Failed")
        XLUtils.writeData(file,"Sheet1",r,7,"Failed")
        XLUtils.fillRedColor(file,"Sheet1",r,7)

    driver.refresh()
    time.sleep(2)