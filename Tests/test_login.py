from Configurations.TestData import TestData
from Pages.LoginPage import LoginPage
import allure

@allure.feature('Login test')
class TestLogin:
    @allure.story('Success login to mail')
    def test_success_login(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        login_page = LoginPage(driver)
        login_page.click_cookie_accepted()
        login_page.fill_login_field(TestData.LOGIN)
        login_page.fill_password_field(TestData.PASSWORD)
        login_page.click_submit_button_main()

        assert login_page.get_pageTitle() == 'Вхідні -\xa0I.UA\xa0'
    @allure.story('Wrong login to authorization to mail')
    def test_with_wrong_login(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        login_page = LoginPage(driver)
        login_page.click_cookie_accepted()
        login_page.fill_login_field(TestData.WRONG_LOGIN)
        login_page.fill_password_field(TestData.PASSWORD)
        login_page.click_submit_button_main()

        assert login_page.get_pageTitle() == 'Паспорт -\xa0I.UA\xa0'

    @allure.story('Wrong password to authorization to mail')
    def test_with_wrong_password(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        login_page = LoginPage(driver)
        login_page.click_cookie_accepted()
        login_page.fill_login_field(TestData.WRONG_LOGIN)
        login_page.fill_password_field(TestData.WRONG_PASSWORD)
        login_page.click_submit_button_main()

        assert login_page.get_pageTitle() == 'Паспорт -\xa0I.UA\xa0'
    @allure.story('Success authorization with pop-up window')
    def test_success_loin_with_popup(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        login_page = LoginPage(driver)
        login_page.click_cookie_accepted()
        login_page.click_submit_button_enter_popup()
        login_page.fill_login_field_in_popup(TestData.LOGIN)
        login_page.fill_password_field_in_popup(TestData.PASSWORD)
        login_page.click_submit_button_in_popup()

        assert login_page.get_pageTitle() == 'І.UA - моя пошта\xa0'
    @allure.story('Test clicking reminder button')
    def test_click_remind_button(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        login_page = LoginPage(driver)
        login_page.click_cookie_accepted()
        login_page.click_remind_button_main()

        assert login_page.get_pageTitle() == 'Паспорт -\xa0I.UA\xa0'
    @allure.story('Test clicking registration button')
    def test_click_registration_button(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        login_page = LoginPage(driver)
        login_page.click_cookie_accepted()
        login_page.click_registration_button_main()

        assert login_page.get_pageTitle() == 'Паспорт -\xa0I.UA\xa0'
