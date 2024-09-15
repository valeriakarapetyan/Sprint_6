import pytest
import allure

from conftest import URL
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.epic("Тестирование страницы заказа")
    @allure.feature("Оформление заказа")
    @pytest.mark.parametrize("button_position, name, surname, address, station, phone, date, comment", [
        ('Нижняя кнопка заказа', 'Олег', 'Витальев', 'ул.Пушкина, 23', 'Лубянка', '+79998586677', '20.09.2024', 'Можно скидочку?'),
        ('Кнопка заказа в шапке', 'Анна', 'Кукушкина', 'ул.Ленина, 1', 'Университет', '+79996766677', '25.09.2024', 'Пожалуйста, перезвоните'),
    ])
    @allure.title("Успешное оформление заказа при нажатии на кнопку: {button_position}")
    @allure.step("Оформление заказа")
    def test_successful_order(self, setup, button_position, name, surname, address, station, phone, date, comment):
        driver = setup
        op = OrderPage(driver)
        if button_position == 'Кнопка заказа в шапке':
            op.click_order_button()
        elif button_position == 'Нижняя кнопка заказа':
            op.click_order_button_on_the_bottom()
        op.fill_order(name, surname, address, station, phone)
        op.fill_order_additional_info(date, comment)
        assert 'Заказ оформлен' in op.get_order_status()


    @allure.title("Проверка перехода на главную страницу")
    @allure.step("Переход на главную страницу")
    def test_transfer_to_main_page(self, setup):
        driver = setup
        op = OrderPage(driver)
        op.transfer_to_main_page()
        assert op.get_current_url() == URL

