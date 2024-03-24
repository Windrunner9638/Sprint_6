import pytest
import allure
import test_data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка создания заказа через хедер')
    @allure.description('При успешном закаже появляется окно с кнопкой "Проверить статус"')
    @pytest.mark.parametrize('name, surname, address, phone', [*test_data.RegistrationDetails.reg_data_order])
    def test_order_true(self, driver, click_cookie, name, surname, address, phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.check_and_click_order_header()
        order_page.set_data_order(name, surname, address, phone)
        order_page.check_and_lick_check_button_next()
        order_page.set_data_order_about_rent()
        order_page.check_visibility_of_button_status()
        text_in_button = order_page.text_in_button_status()
        assert text_in_button == 'Посмотреть статус'

    @allure.title('Проверка открытия формы заказа по кнопки заказа внизу страницы')
    def test_button_order_center_div(self, driver, click_cookie):
        main_page = MainPage(driver)
        main_page.check_button_order_is_clickable()
        main_page.click_button_order_div()
        current_url = main_page.get_current_url()
        assert "https://qa-scooter.praktikum-services.ru/order" in current_url
