# Sprint_6

Проект автоматизации тестирования приложения [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/)

1. Фреймворк: PyTest + Selenium;
2. Структура проекта:
	- tests - директория с тестами;
	- locators - директория с локаторами;
	- pages - директория со страницами;
	- conftest.py - файл с фикстурами;
	- test_data.py - файл с тестовыми данными (URL, credentials);
3. Запуск тестов: `pytest -v`;
   Запуск тестов c формированием отчета: `pytest -v  --alluredir=allure_results`;
   Посмотреть веб версию отчета: `allure serve allure_results`