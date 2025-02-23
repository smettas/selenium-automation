import pytest

@pytest.mark.usefixtures("setup")
class TestTitles:
    #######Parameter and values giving in the parameters  in a tuples[]#############
    @pytest.mark.parametrize("url, title",[
        ("https://www.google.com/","Google"),
        ("https://www.facebook.com/","Facebook – log in or sign up"),
        ("https://www.cricbuzz.com/","Live Cricket Score, Schedule, Latest News, Stats & Videos | Cricbuzz.com"),
        ("https://www.instagram.com/","Instagram"),
        ("https://www.yahoo.com/","Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos")
    ], ids=["Google", "Facebook", "Cricbuzz", "Instagram", "Yahoo"])  #####Id's nothing but a human readable in console given name to test
    def test_titles(self, url, title):
        self.driver.get(url)
        assert self.driver.title==title