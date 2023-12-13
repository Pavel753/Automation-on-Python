from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://34.141.58.52:8080/#/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "login")
    input1.send_keys("zavan@mail.ru")
    time.sleep(1)
    input2 = browser.find_element(By.CSS_SELECTOR, "#password > input")
    input2.send_keys("1234")
    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "p-button-label")
    button.submit()
    time.sleep(1)

    names = browser.find_elements(By.CSS_SELECTOR, ".col-12")

    assert len(names) == 3


finally:

    browser.quit()
