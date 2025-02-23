

########## XLUtils module not required for sql DB. we can write code easily ##########
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.maximize_window()

file="D:\\Sai Work\\Python\\Practice\\simple interest.xlsx"

######Try and Except blocks helps us ...If code is not ececuted then the except block will execute like what we given in in that block
try:
    connection=mysql.connector.connect(host='localhost', port='3306', user='root', passwd='root', database='mydb')
    cursor=connection.cursor()
    cursor.execute("select * from caldata")

    for r in cursor:
        ######## Reading data from Excel #######
        principle=r[0]
        annualRate=r[1]
        periodUnit=r[3]
        periodValue=r[4]
        expectedValue=r[5]

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
        else:
            print("Failed")

        driver.refresh()
except:
    print("Something Interner net collection or DataBase connection problem")