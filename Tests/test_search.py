from Configurations.TestData import TestData
from Pages.MainPage import MainPage


class TestSearch:
    def test_search(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        search_page = MainPage(driver)
        search_page.fill_search_field(TestData.TEXT_TO_SEARCH)
        search_page.click_find_search_button()

        assert search_page.get_pageTitle() == 'Пошук -\xa0I.UA\xa0'
