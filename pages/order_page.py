import random
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class OrderPage(BasePage):
    ORDER_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g'
    ORDER_BUTTON_ON_THE_BOTTOM = By.XPATH, '//button[contains(@class,"Button_Middle")]'
    SCOOTER_LABEL = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'

    # страница заказа
    NAME_INPUT = By.XPATH, '//input[@placeholder="* Имя"]'
    SURNAME_INPUT = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_STATION_INPUT = By.CLASS_NAME, 'select-search__input'
    METRO_STATION_CHOICE = By.CLASS_NAME, 'select-search__select'
    PHONE_INPUT = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'

    # страница деталей заказа
    DATE_INPUT = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD = By.CLASS_NAME, 'Dropdown-root'
    PERIOD_CHOICES = By.CLASS_NAME, 'Dropdown-menu'
    COLOR_CHOICE = By.ID, 'black'
    COMMENT_INPUT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    FINAL_ORDER_BUTTON = By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text() ' \
                                   '= "Заказать"] '
    CONFIRM_ORDER_BUTTON = By.XPATH, '//button[text()="Да"]'
    SUCCESS_MESSAGE = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'

    @allure.step("Клик на кнопку 'Заказать'")
    def click_order_button(self):
        self.find_element(*self.ORDER_BUTTON).click()

    @allure.step("Заполнение имени")
    def fill_order_name(self, name):
        self.find_element(*self.NAME_INPUT).send_keys(name)

    @allure.step("Заполнение фамилии")
    def fill_order_surname(self, surname):
        self.find_element(*self.SURNAME_INPUT).send_keys(surname)

    @allure.step("Заполнение адреса")
    def fill_order_address(self, address):
        self.find_element(*self.ADDRESS_INPUT).send_keys(address)

    @allure.step("Заполнение станции метро")
    def fill_order_metro_station(self, station):
        self.find_element(*self.METRO_STATION_INPUT).click()
        self.find_element(*self.METRO_STATION_INPUT).send_keys(station)
        self.find_element(*self.METRO_STATION_CHOICE).click()

    @allure.step("Заполнение номера телефона")
    def fill_order_phone_number(self, phone):
        self.find_element(*self.PHONE_INPUT).send_keys(phone)

    @allure.step("Клик на кнопку 'Далее'")
    def click_next_button(self):
        self.find_element(*self.NEXT_BUTTON).click()

    @allure.step("Заполнение основной информации по заказу")
    def fill_order_main_info(self, name, surname, address, station, phone):
        self.fill_order_name(name)
        self.fill_order_surname(surname)
        self.fill_order_address(address)
        self.fill_order_metro_station(station)
        self.fill_order_phone_number(phone)
        self.click_next_button()

    @allure.step("Заполнение даты заказа")
    def fill_order_date(self, date):
        self.find_element(*self.DATE_INPUT).send_keys(date)

    @allure.step("Выбор периода заказа")
    def choose_rental_period(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.find_element(*self.RENTAL_PERIOD).click()
        period_elements = self.find_elements(*self.PERIOD_CHOICES)
        chosen_period_element = random.choice(period_elements)
        self.scroll_to_element(chosen_period_element)
        chosen_period_element.click()

    @allure.step("Выбор цвета самоката")
    def choose_color(self):
        self.find_element(*self.COLOR_CHOICE).click()

    @allure.step("Заполнение комментария")
    def fill_order_comment(self, comment):
        self.find_element(*self.COMMENT_INPUT).send_keys(comment)

    @allure.step("Клик на кнопку завершения заказа")
    def click_final_order_button(self):
        self.find_element(*self.FINAL_ORDER_BUTTON).click()

    @allure.step("Клик на кнопку подтверждения заказа")
    def click_confirm_order_button(self):
        self.find_element(*self.CONFIRM_ORDER_BUTTON).click()

    @allure.step("Заполнение дополнительной информации по заказу")
    def fill_order_additional_info(self, date, comment):
        self.wait_for_element_to_be_visible(self.FINAL_ORDER_BUTTON)
        self.fill_order_date(date)
        self.choose_rental_period()
        self.choose_color()
        self.fill_order_comment(comment)
        self.click_final_order_button()
        self.wait_for_element_to_be_visible(self.CONFIRM_ORDER_BUTTON)
        self.click_confirm_order_button()

    @allure.step("Получение статуса заказа")
    def get_order_status(self):
        return self.find_element(*self.SUCCESS_MESSAGE).text

    @allure.step("Клик на кнопку 'Заказать' внизу страницы")
    def click_order_button_on_the_bottom(self):
        self.close_cookie_window()
        self.scroll_to_element(self.find_element(*self.ORDER_BUTTON_ON_THE_BOTTOM))
        self.wait_for_element_to_be_visible(self.ORDER_BUTTON_ON_THE_BOTTOM)
        self.find_element(*self.ORDER_BUTTON_ON_THE_BOTTOM).click()

    @allure.step("Переход на главную страницу через лого Самоката")
    def transfer_to_main_page(self):
        self.click_order_button()
        self.find_element(*self.SCOOTER_LABEL).click()

    @allure.step("Клик на кнопку заказа по позиции: {button_position}")
    def click_order_button_by_position(self, button_position):
        if button_position == 'Кнопка заказа в шапке':
            self.click_order_button()
        elif button_position == 'Нижняя кнопка заказа':
            self.click_order_button_on_the_bottom()
