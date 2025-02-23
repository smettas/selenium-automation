from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get("https://www.flipkart.com/")

all_cookies=driver.get_cookies()
print(len(all_cookies))

#######Printing all cookies based on names and value###########
for all in all_cookies:
    print(all.get("name")," : ",all.get("value"))
print()

#####Adding cookie#########
driver.add_cookie({"name":"Sai", "value":"143"})

#######Deleting all cookies###########
driver.delete_all_cookies()
cookie=driver.get_cookies()
print(f"After deleting all cookies : {len(cookie)}")