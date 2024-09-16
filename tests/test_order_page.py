import pytest
import allure

from conftest import URL


@allure.epic("Тестирование страницы заказа")
class TestOrderPage:

    @allure.feature("Оформление заказа")
    @pytest.mark.parametrize("button_position, name, surname, address, station, phone, date, comment", [
        ('Нижняя кнопка заказа', 'Олег', 'Витальев', 'ул.Пушкина, 23', 'Лубянка', '+79998586677', '20.09.2024',
         'Можно скидочку?'),
        ('Кнопка заказа в шапке', 'Анна', 'Кукушкина', 'ул.Ленина, 1', 'Университет', '+79996766677', '25.09.2024',
         'Пожалуйста, перезвоните'),
    ])
    @allure.title("Успешное оформление заказа при нажатии на кнопку: {button_position}")
    def test_successful_order(self, order_page, button_position, name, surname, address, station, phone, date, comment):
        order_page.click_order_button_by_position(button_position)
        order_page.fill_order_main_info(name, surname, address, station, phone)
        order_page.fill_order_additional_info(date, comment)
        assert 'Заказ оформлен' in order_page.get_order_status()

    @allure.title("Проверка перехода на главную страницу")
    def test_transfer_to_main_page(self, order_page):
        order_page.transfer_to_main_page()
        assert order_page.get_current_url() == URL
