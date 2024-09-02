import pytest
from selenium import webdriver


@pytest.fixture
def firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
