import pytest
import allure
from pages.main_page import MainPage
import test_data


class TestAccordion:

    @allure.title('Проверка соответствия вопроса и ответа в разделе вопросы о важном')
    @pytest.mark.parametrize('number, accordion_number, result', [*test_data.Accordion.accordion_data])
    def test_accordion(self, driver, click_cookie, number, accordion_number, result):
        main_page = MainPage(driver)
        main_page.check_button_order_in_header_is_clickable()
        main_page.click_on_element(number)
        text = main_page.find_my_element(accordion_number)
        assert text.text == result
