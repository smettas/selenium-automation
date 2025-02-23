import pytest

####### Multiple Parameterized Decorators (Cartesian Product) #############
@pytest.mark.parametrize("browser",["chrome", "edge"], scope="class")
@pytest.mark.usefixtures("browsers")
class TestMultiTitles:
    @pytest.mark.parametrize("url, title",[
        ("https://www.google.com/","Google"),
        ("https://www.facebook.com/","Facebook – log in or sign up"),
        ("https://www.cricbuzz.com/","Live Cricket Score, Schedule, Latest News, Stats & Videos | Cricbuzz.com"),
        ("https://www.instagram.com/","Instagram"),
        ("https://www.yahoo.com/","Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos")
    ], ids=["Google", "Facebook", "Cricbuzz", "Instagram", "Yahoo"])  #####Id's nothing but a human readable in console given name to test
    def test_titles(self, browser, url, title):
        self.driver.get(url)
        assert self.driver.title==title

### Command for getting log files ##### configuration given in the pytest.ini file
###### pytest -k TestMultiTitles -n 10 -v --html="multi_browsers.html" --self-contained-html --show-capture=log  ######