import os
from ssl import Options
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Check if running in Jenkins environment
HEADLESS_MODE = os.getenv("PYTEST_HEADLESS", "true").lower()=="true"

chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()

if HEADLESS_MODE:
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Prevent some CI issues
    chrome_options.add_argument("--no-sandbox")   # Required for some CI/CD environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents shared memory issues

driver = None
def setup_module(module):
    global driver
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title=="Google"  ####### Pass

def test_google_url():
    assert driver.current_url=="https://www.google.com/"  ####### Fail

