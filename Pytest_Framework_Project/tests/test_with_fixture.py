import pytest

####### setup() is in conftest.py class......... driver instance there only i given #########

@pytest.mark.usefixtures("setup")
class TestTitles:
    @pytest.mark.titles
    def test_google(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title=="Google"

    @pytest.mark.titles
    def test_facebook(self):
        self.driver.get("https://www.facebook.com/")
        assert self.driver.title=="Facebook – log in or sign up"

    @pytest.mark.titles
    def test_cricbuzz(self):
        self.driver.get("https://www.cricbuzz.com/")
        assert self.driver.title=="Live Cricket Score, Schedule, Latest News, Stats & Videos | Cricbuzz.com"

    @pytest.mark.titles
    def test_insta(self):
        self.driver.get("https://www.instagram.com/")
        assert self.driver.title=="Instagram"

    @pytest.mark.titles
    def test_yahoo(self):
        self.driver.get("https://www.yahoo.com/")
        assert self.driver.title=="Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos"