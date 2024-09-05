from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class MainPage:
    textbox_search_field = (By.ID, "searchQ")
    find_search_button = (By.XPATH, "//input[@value='Знайти']")
    weather_button = (By.XPATH, "//a[contains(text(),'Погода на тиждень')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_search_field(self, text):
        self.driver.find_element(*self.textbox_search_field).send_keys(text)

    def click_find_search_button(self):
        self.driver.find_element(*self.find_search_button).click()

    def click_weather_button(self):
        self.driver.find_element(*self.weather_button).click()

    def get_pageTitle(self):
        return self.driver.title
