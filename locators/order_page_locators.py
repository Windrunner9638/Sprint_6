from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поле ввод имени
    NAME = [By.XPATH, '//input[@placeholder="* Имя"]']

    # Поле ввод фамилии
    SURNAME = [By.XPATH, '//input[@placeholder="* Фамилия"]']

    # Поле ввод адреса
    ADDRESS = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']

    # Поле выбора станции
    METRO_STATION = [By.XPATH, '//input[@placeholder="* Станция метро"]']

    # Ввод телефона
    PHONE = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']

    # Поле выбора даты доставки
    DATE = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']

    # Текущая дата
    TODAY = [By.CLASS_NAME, 'react-datepicker__day--today']

    # Поле выбора периода аренды
    RENTAL_PERIOD = [By.CLASS_NAME, 'Dropdown-placeholder']

    # Время аренды
    RENTAL_PERIOD_CHOOSE = [By.XPATH, '//div[@class = "Dropdown-option" and text()="трое суток"]']

    # Чекбокс черного цвета самоката
    BLACK_COLOR = [By.ID, 'black']

    # Кнопка Далее
    BUTTON_NEXT = [By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text()= "Далее"]']

    # Кнопка Заказать
    BUTTON_ORDER = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()= "Заказать"]']

    # Кнопка Да
    BUTTON_YES = [By.XPATH, './/button[text()= "Да"]']

    # Кнопка Посмотреть статус
    BUTTON_STATUS = [By.XPATH, './/button[text()= "Посмотреть статус"]']

    # Метро Косомольская в выпадающем списке
    METRO_STATION_KOMSOMOLSKAYA = [By.XPATH, f'//div[text()= "Комсомольская"]']