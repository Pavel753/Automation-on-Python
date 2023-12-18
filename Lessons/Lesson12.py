# Параметры запусков тестов -m запустить тест с нужной маркировкой -v (verbose, то есть подробный) в отчёт добавится
# дополнительная информация со списком тестов и статусом их прохождения -s позволяет увидеть текст, который выводится
# командой print()
# Параметр -r принимает ряд символов после себя.
# f - упавшие (добавляет раздел FAILED)
# E - ошибки (добавляет раздел ERROR)
# s - пропущенные (добавляет раздел SKIPPED)
# x - тесты XFAIL (добавляет раздел XFAIL)
# X - тесты XPASS (добавляет раздел XPASS)
# p - успешные (passed)
# P - успешные (passed) с выводом

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://34.141.58.52:8080/#/login"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestLogin:

    # @pytest.mark.smoke
    # @pytest.mark.win10
    def test_input_login(self, browser):
        browser.get(link)
        input1 = browser.find_element(By.ID, "login")
        input1.send_keys("zavan@mail.ru")

    # @pytest.mark.smoke
    def test_input_password(self, browser):
        browser.get(link)
        input2 = browser.find_element(By.CSS_SELECTOR, "#password > input")
        input2.send_keys("1234")

    # @pytest.mark.smoke
    def test_submit_button(self, browser):
        browser.get(link)
        button = browser.find_element(By.CLASS_NAME, "p-button-label")
        button.submit()
        browser.save_screenshot('result1.png')

    @pytest.mark.xfail
    def test_pets_have_names(self, browser):
        names = browser.find_elements(By.CSS_SELECTOR, "p-grid p-nogutter grid grid-nogutter.product.name")

        for i in range(len(names)):
            assert names[i].text != ''

# Параметризация тестов
# @pytest.mark.parametrize('os', ['win10', 'win11'])
#def test_pets(browser, os):

# Flaky-тесты
# pip install pytest_rerunfailures
"--reruns n"
