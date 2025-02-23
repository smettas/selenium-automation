from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.Config import Config

class BasePage(Config):   # Inheriting config values
    def __init__(self, driver): 
        self.driver = driver    # Assigning the WebDriver instance

    # Generic method to enter text in input fields
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, self.TIME_OUT).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    # Generic method to click elements
    def do_click(self, by_locator):
        WebDriverWait(self.driver, self.TIME_OUT).until(EC.presence_of_element_located(by_locator)).click()
        


"""
🔹 Comments:

1.Base class for all pages in the framework.
2.do_send_keys() → Waits for the input field and enters text.
3.do_click() → Waits for the element and clicks on it.
4.Extends Config class for reusing timeouts and URL.

"""