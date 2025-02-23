import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.titles
def test_google():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title=="Google"
    driver.quit()

@pytest.mark.titles
def test_facebook():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    assert driver.title=="Facebook – log in or sign up"
    driver.quit()

@pytest.mark.titles
def test_cricbuzz():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.cricbuzz.com/")
    assert driver.title=="Live Cricket Score, Schedule, Latest News, Stats & Videos | Cricbuzz.com"
    driver.quit()

@pytest.mark.titles
def test_insta():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/")
    assert driver.title=="Instagram"
    driver.quit()

@pytest.mark.titles
def test_yahoo():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.yahoo.com/")
    assert driver.title=="Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos"
    driver.quit()