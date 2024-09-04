from selenium.webdriver.common.by import By
from Pages.MainPage import MainPage


class LoginPage(MainPage):
    textbox_usermail_on_main = (By.XPATH, "//input[@name='login']")
    textbox_password_on_main = (By.XPATH, "//input[@name='pass']")
    submit_button_on_main = (By.XPATH, "//input[@title='Вхід на пошту']")
    button_enter_popup_on_main = (By.XPATH, "//a[contains(text(),'Вхід')]")
    textbox_usermail_in_popup = (By.XPATH, "//form[@name='lFloat']//input[@name='login']")
    textbox_password_in_popup = (By.XPATH, "//form[@name='lFloat']//input[@name='pass']")
    submit_button_enter_popup = (By.XPATH, "//form[@name='lFloat']//input[@value='Увійти']")
    remind_button_on_main = (By.XPATH, "//a[@class='float_right']")
    registration_button_on_main = (By.XPATH, "//div[@class='content clear']//a[contains(text(),'Реєстрація')]")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_login_field(self, username):
        self.driver.find_element(*self.textbox_usermail_on_main).send_keys(username)

    def fill_login_field_in_popup(self, usermail):
        self.driver.find_element(*self.textbox_usermail_in_popup).send_keys(usermail)

    def fill_password_field(self, password):
        self.driver.find_element(*self.textbox_password_on_main).send_keys(password)

    def fill_password_field_in_popup(self, password):
        self.driver.find_element(*self.textbox_password_in_popup).send_keys(password)

    def click_submit_button_main(self):
        self.driver.find_element(*self.submit_button_on_main).click()

    def click_submit_button_enter_popup(self):
        self.driver.find_element(*self.button_enter_popup_on_main).click()

    def click_submit_button_in_popup(self):
        self.driver.find_element(*self.submit_button_enter_popup).click()

    def click_remind_button_main(self):
        self.driver.find_element(*self.remind_button_on_main).click()

    def click_registration_button_main(self):
        self.driver.find_element(*self.registration_button_on_main).click()
