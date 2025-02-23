import pytest
from pages.HomePage import HomePage
from tests.BaseTest import BaseTest

class HomePageTest(BaseTest):

    def test_home_page_link(self):
        home_page = HomePage(self.driver)
        home_page.home_page()  # Click home page link
        assert "orangehrm" in self.driver.current_url.lower()  # Verify home page loads

"""
🔹 Comments:

1.Verifies Home Page navigation by clicking on the link.
2.Uses assert to confirm that the correct page is loaded.
"""