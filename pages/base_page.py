import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_data import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл в низ страницы')
    def scroll_to_down_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Нажать на элемент
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    # Ожидание пока элемент не станет кликабельным
    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))

    # Найти элемент
    def find_my_element(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Смена страницы')
    def switch_pages(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(Urls.dzen_url))

    @allure.step('Получение текущего url')
    def get_current_url(self):
        return self.driver.current_url

    def set_field_by_locator(self, locator, name):
        self.driver.find_element(*locator).send_keys(name)

    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text
