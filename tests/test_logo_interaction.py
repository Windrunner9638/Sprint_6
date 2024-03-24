import allure
from pages.main_page import MainPage


class TestLogo:

    @allure.title('Проверка перехода на "https://dzen.ru/" при клике на логотип Yandex')
    def test_logo_redirect_dzen_true(self, driver, click_cookie):
        main_page = MainPage(driver)
        main_page.check_logo_yandex_is_clickable()
        main_page.click_logo_yandex()
        main_page.switch_pages()
        current_url = main_page.get_current_url()
        assert "https://dzen.ru/" in current_url

    @allure.title('Проверка перехода на "https://qa-scooter.praktikum-services.ru/" при клике на логотип Самокат')
    def test_logo_go_to_start_page_true(self, driver, click_cookie):
        main_page = MainPage(driver)
        main_page.check_button_order_in_header_is_clickable()
        main_page.click_button_order_header()
        main_page.click_logo_scooter()
        current_url = main_page.get_current_url()
        assert "https://qa-scooter.praktikum-services.ru/" in current_url
