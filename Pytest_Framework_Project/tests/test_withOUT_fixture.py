from ssl import Options
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ops=webdriver.ChromeOptions()
ops.add_argument("--headless")

driver = None
def setup_module(module):
    global driver
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service, options=ops)
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title=="Google"  ####### Pass

def test_google_url():
    assert driver.current_url=="https://www.google.com/"  ####### Fail

