import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://34.141.58.52:8080/#/login"


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# class TestLogin:
#
#     def test_input_login(self, browser):
#         browser.get(link)
#         input1 = browser.find_element(By.ID, "login")
#         input1.send_keys("zavan@mail.ru")
#
#     def test_input_password(self, browser):
#         browser.get(link)
#         input2 = browser.find_element(By.CSS_SELECTOR, "#password > input")
#         input2.send_keys("1234")
#
#     def test_submit_button(self, browser):
#         browser.get(link)
#         button = browser.find_element(By.CLASS_NAME, "p-button-label")
#         button.submit()
#         browser.save_screenshot('result1.png')
