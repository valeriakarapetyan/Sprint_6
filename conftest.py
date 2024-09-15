from selenium import webdriver
import pytest

URL = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture
def setup():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()
