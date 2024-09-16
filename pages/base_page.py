import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    COOKIE_WINDOW = By.ID, 'rcc-confirm-button'

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ищем элемент по локатору")
    def find_element(self, *element):
        return self.driver.find_element(*element)

    @allure.step("Ищем элементы")
    def find_elements(self, *element):
        return self.driver.find_elements(*element)

    @allure.step("Закрываем окно с куками")
    def close_cookie_window(self):
        self.find_element(*self.COOKIE_WINDOW).click()

    @allure.step("Ждем, пока элемент будет виден")
    def wait_for_element_to_be_visible(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_new_window(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step("Получаем текущий адрес")
    def get_current_url(self):
        return self.driver.current_url
