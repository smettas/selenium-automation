import pytest

from selenium.webdriver.common.by import By
from config.Config import Config
from pages import BasePage
from pages.BasePage import BasePage

class LoginPage(BasePage):

    # Locators for login page elements
    username = (By.XPATH,"//input[@placeholder='Username']")
    password = (By.XPATH,"//input[@placeholder='Password']")
    login_button = (By.XPATH,"//button[normalize-space()='Login']")
    #page_title = "OrangeHRM"

    def __init__(self, driver):
        super().__init__(driver)  # Call BasePage constructor
        self.driver.get(Config.BASE_URL)  # Navigate to the login page

    # Method to perform login
    def do_login(self, username, password):
        self.do_send_keys(self.username, username)  # Enter username
        self.do_send_keys(self.password, password)  # Enter password
        self.do_click(self.login_button)  # Click login button


"""
🔹 Comments:

1.Implements POM (Page Object Model) for the Login Page.
2.Stores element locators and methods to interact with them.
3.Uses do_send_keys() and do_click() from BasePage for reusability.
4.Navigates to the Login URL during initialization.

"""