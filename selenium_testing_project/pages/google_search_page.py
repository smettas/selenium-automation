from selenium.webdriver.common.by import By

class GoogleSearchPage:
    # Locators for Google search page
    SEARCH_BOX = (By.NAME, "q")
    RESULTS = (By.CSS_SELECTOR, "h3")

    def __init__(self, driver):
        self.driver = driver

    def enter_search_query(self, query):
        search_box = self.driver.find