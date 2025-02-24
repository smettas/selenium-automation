import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

ops=webdriver.ChromeOptions()
opss=webdriver.EdgeOptions()
ops.add_argument("--headless")
opss.add_argument("--headless")

@pytest.fixture(scope="class")
def setup(request):  #######requrest name we need to pass......
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service, options=ops)
    driver.implicitly_wait(10)  
    request.cls.driver=driver   ########## Assigning the driver to the test class instance 
    yield driver        ###### Yield before driver starts.... Yield after driver closes #######
    driver.quit() 


@pytest.fixture(scope="function")
def browsers(request, browser):  #######requrest name we need to pass......
    if browser=="chrome":
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service, options=ops)
    elif browser=="edge":
        service=EdgeService(EdgeChromiumDriverManager().install())
        driver=webdriver.Edge(service=service, options=opss)
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
