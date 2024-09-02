import pytest

from Configarations.TestData import TestData
from Pages.MainPage import MainPage


class TestLogin:
    def test_success_login(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        main_page = MainPage(driver)
        main_page.fill_login_field(TestData.LOGIN)
        main_page.fiil_password_field(TestData.PASSWORD)
        main_page.click_submit_button()

        assert main_page.get_pageTitle() == 'Вхідні -\xa0I.UA\xa0'
