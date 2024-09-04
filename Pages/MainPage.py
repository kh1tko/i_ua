from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.textbox_usermail = (By.XPATH, "//input[@name='login']")
        self.textbox_password = (By.XPATH, "//input[@name='pass']")
        self.submit_button_main = (By.XPATH, "//input[@title='Вхід на пошту']")
        self.button_enter_popup = (By.XPATH, "//a[contains(text(),'Вхід')]")
        self.textbox_usermail_in_popup = (By.XPATH, "//form[@name='lFloat']//input[@name='login']")
        self.textbox_password_in_popup = (By.XPATH, "//form[@name='lFloat']//input[@name='pass']")
        self.submit_button_enter_popup = (By.XPATH, "//form[@name='lFloat']//input[@value='Увійти']")

    def fill_login_field(self, username):
        self.driver.find_element(*self.textbox_usermail).send_keys(username)

    def fill_login_field_in_popup(self, usermail):
        self.driver.find_element(*self.textbox_usermail_in_popup).send_keys(usermail)

    def fill_password_field(self, password):
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def fill_password_field_in_popup(self, password):
        self.driver.find_element(*self.textbox_password_in_popup).send_keys(password)

    def click_submit_button_main(self):
        self.driver.find_element(*self.submit_button_main).click()

    def click_submit_button_enter_popup(self):
        self.driver.find_element(*self.button_enter_popup).click()

    def click_submit_button_in_popup(self):
        self.driver.find_element(*self.submit_button_enter_popup).click()

    def get_pageTitle(self):
        return self.driver.title
