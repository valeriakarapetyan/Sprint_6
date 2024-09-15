from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    COOKIE_WINDOW = By.ID, 'rcc-confirm-button'

    def __init__(self, driver):
        self.driver = driver

    def close_cookie_window(self):
        self.driver.find_element(*self.COOKIE_WINDOW).click()

    def wait_for_element_to_be_visible(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_window(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url
