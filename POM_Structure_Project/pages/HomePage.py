
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):

    # Locator for home page link
    home_page_link = (By.LINK_TEXT,"OrangeHRM, Inc")

    def __init__(self, driver):
        super().__init__(driver)    # Locator for home page link

    # Method to click home page link
    def home_page(self):
        self.do_click(self.home_page_link)


"""
🔹 Comments:

1.Implements POM for the Home Page.
2.Provides a method to click the home page link.
3.Inherits BasePage for reusable methods.
"""