from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    YANDEX_LABEL = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'

    # локаторы вопросов
    FIRST_QUESTION = By.ID, 'accordion__heading-0'
    SECOND_QUESTION = By.ID, 'accordion__heading-1'
    THIRD_QUESTION = By.ID, 'accordion__heading-2'
    FOURTH_QUESTION = By.ID, 'accordion__heading-3'
    FIFTH_QUESTION = By.ID, 'accordion__heading-4'
    SIXTH_QUESTION = By.ID, 'accordion__heading-5'
    SEVENTH_QUESTION = By.ID, 'accordion__heading-6'
    EIGHTH_QUESTION = By.ID, 'accordion__heading-7'

    # локаторы ответов
    FIRST_ANSWER = By.XPATH, '//*[@aria-labelledby="accordion__heading-0"]'
    SECOND_ANSWER = By.XPATH, '//*[@aria-labelledby="accordion__heading-1"]'
    THIRD_ANSWER = By.XPATH, '//*[@aria-labelledby="accordion__heading-2"]'
    FOURTH_ANSWER = By.XPATH, '//*[@aria-labelledby="accordion__heading-3"]'
    FIFTH_ANSWER = By.XPATH, '//*[@aria-labelledby="accordion__heading-4"]'
    SIXTH_ANSWER = By.XPATH, '//*[@aria-labelledby="accordion__heading-5"]'
    SEVENTH_ANSWER = By.XPATH, '//*[@aria-labelledby="accordion__heading-6"]'
    EIGHTH_ANSWER = By.XPATH, '//*[@aria-labelledby="accordion__heading-7"]'

    QUESTIONS = [
        FIRST_QUESTION,
        SECOND_QUESTION,
        THIRD_QUESTION,
        FOURTH_QUESTION,
        FIFTH_QUESTION,
        SIXTH_QUESTION,
        SEVENTH_QUESTION,
        EIGHTH_QUESTION
    ]

    ANSWERS = [
        FIRST_ANSWER,
        SECOND_ANSWER,
        THIRD_ANSWER,
        FOURTH_ANSWER,
        FIFTH_ANSWER,
        SIXTH_ANSWER,
        SEVENTH_ANSWER,
        EIGHTH_ANSWER
    ]

    @allure.step("Получение ответа на вопрос")
    def get_answer_to_question(self, question_number):
        question = self.QUESTIONS[question_number]
        answer = self.ANSWERS[question_number]
        self.scroll_to_element(self.find_element(*question))
        self.wait_for_element_to_be_visible(question)
        self.find_element(*question).click()
        self.wait_for_element_to_be_visible(answer)
        return self.find_element(*answer).text

    @allure.step("Переход на страницу Дзена")
    def transfer_to_dzen(self):
        self.find_element(*self.YANDEX_LABEL).click()
        self.switch_to_new_window('https://dzen.ru/?yredirect=true')
