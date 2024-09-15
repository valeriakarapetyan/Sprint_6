import pytest
import allure

from pages.main_page import MainPage


class TestMainPage:

    @allure.epic("Тестирование главной страницы")
    @allure.feature("Часто задаваемые вопросы")
    @pytest.mark.parametrize("question_number, expected_answer", [
        (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать '
            'несколько заказов — один за другим.'),
        (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды '
            'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, '
            'суточная аренда закончится 9 мая в 20:30.'),
        (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без '
            'передышек и во сне. Зарядка не понадобится.'),
        (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    @allure.title("Проверка соответствия ответа вопросу")
    @allure.step("Проверка корректности ответа")
    def test_get_correct_answer(self, setup, question_number, expected_answer):
        driver = setup
        mp = MainPage(driver)
        mp.close_cookie_window()
        answer = mp.get_answer_to_question(question_number)
        assert answer == expected_answer

    @allure.title("Проверка перехода на Дзен")
    @allure.step("Переход на страницу Дзен")
    def test_transfer_to_dzen(self, setup):
        driver = setup
        mp = MainPage(driver)
        mp.transfer_to_dzen()
        assert mp.get_current_url() == 'https://dzen.ru/?yredirect=true'
