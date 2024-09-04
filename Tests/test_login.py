import pytest

from Configarations.TestData import TestData
from Pages.MainPage import MainPage


class TestLogin:
    def test_success_login(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        main_page = MainPage(driver)
        main_page.fill_login_field(TestData.LOGIN)
        main_page.fill_password_field(TestData.PASSWORD)
        main_page.click_submit_button_main()

        assert main_page.get_pageTitle() == 'Вхідні -\xa0I.UA\xa0'

    def test_with_wrong_login(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        main_page = MainPage(driver)
        main_page.fill_login_field(TestData.WRONG_LOGIN)
        main_page.fill_password_field(TestData.PASSWORD)
        main_page.click_submit_button_main()

        assert main_page.get_pageTitle() == 'Паспорт -\xa0I.UA\xa0'

    def test_with_wrong_password(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        main_page = MainPage(driver)
        main_page.fill_login_field(TestData.WRONG_LOGIN)
        main_page.fill_password_field(TestData.WRONG_PASSWORD)
        main_page.click_submit_button_main()

        assert main_page.get_pageTitle() == 'Паспорт -\xa0I.UA\xa0'

    def test_success_loin_with_popup(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        main_page = MainPage(driver)
        main_page.click_submit_button_enter_popup()
        main_page.fill_login_field_in_popup(TestData.LOGIN)
        main_page.fill_password_field_in_popup(TestData.PASSWORD)
        main_page.click_submit_button_in_popup()

        assert main_page.get_pageTitle() == 'І.UA - моя пошта\xa0'
