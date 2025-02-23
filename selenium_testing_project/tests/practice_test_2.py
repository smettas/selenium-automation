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

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='product_3186']").click()
time.sleep(2)

driver.find_element(By.ID,"travname").send_keys("Metta")
driver.find_element(By.NAME,"travlastname").send_keys("Sai Krishna")
driver.find_element(By.CSS_SELECTOR,"textarea#order_comments").send_keys("This is sample test case")

driver.find_element(By.ID,"dob").click()
time.sleep(2)
month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
month.select_by_visible_text("Apr")
year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
year.select_by_visible_text("1997")
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text=="24":
        date.click()
        break

driver.find_element(By.XPATH,"//input[@id='sex_1']").click()
driver.find_element(By.XPATH,"//label[normalize-space()='One Way']").click()
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Hyderabad")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("Dhone")

driver.find_element(By.ID,"departon").click()
time.sleep(2)
dep_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
dep_month.select_by_visible_text("May")
dep_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
dep_year.select_by_visible_text("2025")
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text=="23":
        date.click()
        break

#driver.find_element(By.XPATH,"(//b[@role='presentation'])[6]").click()
driver.find_element(By.XPATH,"(//span[@aria-owns='select2-reasondummy-results']").click()
purpose=driver.find_elements(By.XPATH,"//li[@role='option']")
for p in purpose:
    if p.text=="Prank a friend":
        p.click()
        break

time.sleep(10)

driver.find_element(By.XPATH,"//input[@id='deliverymethod_3']").click()
driver.find_element(By.ID,"billname").send_keys("Sai Digital")
driver.find_element(By.ID,"billing_phone").send_keys("7856564582")
driver.find_element(By.ID,"billing_email").send_keys("msadbisbhdh@gmail.com")
print("Upto here executed")

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countries=driver.find_elements(By.XPATH,"//li[@class='select2-results__option' and @role='option']")
for country in countries:
    if country.text=="Pakistan":
        country.click()
        break

driver.find_element(By.ID,"billing_address_1").send_keys("6-120")
driver.find_element(By.XPATH,"//input[@id='billing_address_2']").send_keys("Shankar Nagar")
driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("Hyderabad")

driver.find_element(By.XPATH,"//span[@id='select2-billing_state-container']")
states=driver.find_elements(By.XPATH,"//li[@role='option' and @class='select2-results__option']")
for state in states:
    if state.text=="Punjab":
        state.click()
        break
print("Upto here exceuted: 2")
driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("518422")

fare = driver.find_element(By.XPATH,"//li[@class='product-item selected']//span[@class='woocommerce-Price-amount amount']")
total_fare = driver.find_element(By.XPATH,"//table[@class='shop_table woocommerce-checkout-review-order-table']/tfoot/tr[2]/td")
if fare==total_fare:
    place_order=driver.find_element(By.XPATH,"//button[@id='place_order']")
    place_order.click()
else:
    print("The actual fare and expected fare is different, Please check the cart and try later")

input()