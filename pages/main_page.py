import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Проверяем кликабельность кнопки заказа из хедера')
    def check_button_order_in_header_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Проверяем кликабельность кнопки заказа внизу страницы')
    def check_button_order_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.BUTTON_ORDER_CENTER_DIV)

    @allure.step('Проверяем кликабельность логотипа "Yandex"')
    def check_logo_yandex_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.LOGO_YANDEX)

    @allure.step('Кликаем по лого Яндекса')
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Кликаем по кнопке "Заказать" в хедере')
    def click_button_order_header(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def click_button_order_div(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDER_CENTER_DIV)

    @allure.step('Кликаем по лого самоката')
    def click_logo_scooter(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Проверяем кликабельность и кликаем по кнопке заказа из хедера"')
    def check_and_click_order_header(self):
        self.check_button_order_in_header_is_clickable()
        self.click_button_order_header()
