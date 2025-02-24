import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Check if running in Jenkins environment
HEADLESS_MODE = os.getenv("PYTEST_HEADLESS", "true").lower()=="true"

chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()

if HEADLESS_MODE:
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Prevent some CI issues
    chrome_options.add_argument("--no-sandbox")   # Required for some CI/CD environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents shared memory issues

    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")  # Prevent some CI issues
    edge_options.add_argument("--no-sandbox")   # Required for some CI/CD environments
    edge_options.add_argument("--disable-dev-shm-usage")  # Prevents shared memory issues
    
@pytest.fixture(scope="class")
def setup(request):  #######requrest name we need to pass......
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)  
    request.cls.driver=driver   ########## Assigning the driver to the test class instance 
    yield driver        ###### Yield before driver starts.... Yield after driver closes #######
    driver.quit() 


@pytest.fixture(scope="function")
def browsers(request, browser):  #######requrest name we need to pass......

    ####### Fixture for setting up browser based on parameter #####
    driver = None
    if browser=="chrome":
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service, options=chrome_options)
    elif browser=="edge":
        service=EdgeService(EdgeChromiumDriverManager().install())
        driver=webdriver.Edge(service=service, options=edge_options)

    if driver:    
        driver.implicitly_wait(10)  
        request.cls.driver=driver   ########## Assigning the driver to the test class instance 
        yield driver        ###### Yield before driver starts.... Yield after driver closes #######
        driver.quit() 




# ######## Adding Screenshots for Failed Tests #########

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("setup")  # Get the WebDriver instance
#         if driver:
#             driver.save_screenshot(f"screenshots/{item.name}.png")


# #pytest --html=report.html --self-contained-html -v ######## In console


# #pytest --html=report.html -v && start report.html ......
# # #6️⃣ Opening the Report AutomaticallyYou can configure Pytest to open the report after execution:
