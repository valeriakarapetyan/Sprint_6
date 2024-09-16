from selenium import webdriver
import pytest
from pages.order_page import OrderPage
from pages.main_page import MainPage

URL = 'https://qa-scooter.praktikum-services.ru/'


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    firefox = webdriver.Firefox(options=options)
    firefox.get(URL)
    firefox.maximize_window()
    yield firefox
    firefox.quit()

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

