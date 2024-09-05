import time

from Pages.MainPage import MainPage
from Configurations.TestData import TestData
from Pages.WeatherPage import WeatherPage


class TestWeatherPage:
    def test_weather_page(self, firefox):
        driver = firefox
        driver.get(TestData.URL)

        main_page = MainPage(driver)
        main_page.click_weather_button()
        weather_page = WeatherPage(driver)

        weather_page.click_change_city_weather_menu()
        weather_page.click_chosen_city_weather()
        result = weather_page.get_check_chosen_city_weather()

        assert result == 'Погода у Полтаві'
