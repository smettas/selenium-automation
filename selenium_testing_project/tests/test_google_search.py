import pytest
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(5)
    yield driver    
    driver.quit()


def test_google_search(driver):
    driver.get("https://www.google.com")
    time.sleep(5)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium 4 Python")
    search_box.send_keys(Keys.RETURN)


    #Verify results appear
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0, "No search results found"