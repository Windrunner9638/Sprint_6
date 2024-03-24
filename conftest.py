import pytest
from selenium.webdriver.firefox import webdriver
from selenium import webdriver
import test_data
from locators.main_page_locators import MainPageLocators


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    driver.get(test_data.Urls.url_main)
    yield driver
    driver.quit()


@pytest.fixture
def click_cookie(driver):
    driver.find_element(*MainPageLocators.COOKIE_LOCATOR).click()
