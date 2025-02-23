import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

# Fixture for browser setup and teardown
@pytest.fixture(scope="function")
def browsers(request, browser):
    if browser=="chrome":
        service=ChromeService(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
    elif browser=="edge":
        service=EdgeService(EdgeChromiumDriverManager().install())
        driver=webdriver.Edge(service=  service)
    else:
        raise ValueError("Unsupported browser: " + browser)
    
    request.cls.driver=driver  # Return driver instance to the test
    yield driver
    driver.quit()   # Cleanup - Close browser after test execution

