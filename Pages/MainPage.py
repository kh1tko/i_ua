from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.textbox_username = (By.XPATH, "//input[@name='login']")
        self.textbox_password = (By.XPATH, "//input[@name='pass']")
        self.submit_button = (By.XPATH, "//input[@title='Вхід на пошту']")

    def fill_login_field(self, username):
        self.driver.find_element(*self.textbox_username).send_keys(username)

    def fiil_password_field(self, password):
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    def get_pageTitle(self):
        return self.driver.title
