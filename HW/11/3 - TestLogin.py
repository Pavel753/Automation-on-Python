import pytest
from credentions import login, password
from selenium.webdriver.common.by import By

link = "http://34.141.58.52:8080/#/login"


class TestLogin:

    @pytest.mark.smoke
    def test_input_login(self, browser):
        browser.get(link)
        input1 = browser.find_element(By.ID, "login")
        input1.send_keys(login)

    @pytest.mark.smoke
    def test_input_password(self, browser):
        browser.get(link)
        input2 = browser.find_element(By.CSS_SELECTOR, "#password > input")
        input2.send_keys(password)

    @pytest.mark.regress
    def test_submit_button(self, browser):
        browser.get(link)
        button = browser.find_element(By.CLASS_NAME, "p-button-label")
        button.submit()
        browser.save_screenshot('result3.png')
