from selenium.webdriver.common.by import By
from Pages.MainPage import MainPage


class WeatherPage(MainPage):
    change_city_weather_menu = (By.ID, 'all_cities_button')
    chosen_city_weather = (By.CSS_SELECTOR, "a[href='/Poltava/']")
    check_chosen_city_weather = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        super().__init__(driver)

    def click_change_city_weather_menu(self):
        self.driver.find_element(*self.change_city_weather_menu).click()

    def click_chosen_city_weather(self):
        self.driver.find_element(*self.chosen_city_weather).click()

    def get_check_chosen_city_weather(self):
        element = self.driver.find_element(*self.check_chosen_city_weather).text
        return element
