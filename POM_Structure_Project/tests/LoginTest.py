import pytest

from config.Config import Config
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class LoginTest(BaseTest):
    
    def test_login(self):
        login_page = LoginPage(self.driver)  # Initialize LoginPage with driver
        login_page.do_login(Config.USER_NAME, Config.PASSWORD)  # Initialize LoginPage with driver
        assert login_page.AFTER_LOGIN_URL==self.driver.current_url()  # Initialize LoginPage with driver

"""
🔹 Comments:

1.Creates LoginPage instance to interact with the login page.
2.Calls do_login() with configured credentials.
3.Asserts that login is successful by checking the dashboard URL.
"""