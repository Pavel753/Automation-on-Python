# https://chrome.google.com/webstore/detail/element-locator/pldlfgnilfdheajekfphjkjeooignhkc?hl=en
import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#
# link = "http://34.141.58.52:8080/#/login"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.XPATH, "//*[@id='login']")
#     input1.send_keys("qwerty@mail.ru")
#     time.sleep(5)
#     input2 = browser.find_element(By.CSS_SELECTOR, "div#password > input")
#     input2.send_keys("1234")
#     time.sleep(5)
#     button = browser.find_element(By.CLASS_NAME, "p-button-label")
#     button.submit()
#     time.sleep(5)
#     pet = browser.find_element(By.XPATH, "//*[@id='app']/main/div/div/div[2]/div/div[1]")
#
#     response = requests.get('http://34.141.58.52:8080/#/profile')
#
#     r = response.status_code
#     assert response.status_code == 200
#
#     browser.save_screenshot('result3.png')
#
# finally:
#
#     browser.quit()

# Фикстуры
import pytest


#
#
# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.set_headless(True)
#     return chrome_options
#
#
@pytest.fixture()
def return_data():
    return 28


def test_return_data(return_data):
    assert return_data == 28

# text_to_be_present_in_element ожидание определённого текста внутри указанного элемента
#
# text_to_be_present_in_element_value ожидание определённого текста внутри атрибута value элемента
#
# frame_to_be_available_and_switch_to_it ожидание появления iframe на странице и переключение на него
#
# invisibility_of_element_located ожидание невидимости элемента, найденного по указанному локатору
#
# title_is ожидание, что заголовок окна браузер равен указанной строке
#
# title_contains ожидание, что заголовок окна содержит определённую строку текста
#
# presence_of_element_located Ожидание присутствия элемента в структуре документа
#
# visibility_of_element_located Ожидание видимости элемента на экране
#
# visibility_of ожидание видимости элемента WebElement
#
# element_to_be_selected ожидание, что элемент в выпадающем списке выбран
#
# element_located_to_be_selected то же, что и предыдущая функция, но указывать элемент нужно через функции поиска
#
# element_selection_state_to_be ожидание, что элемент выпадающего списка имеет определённое состояние
#
# element_located_selection_state_to_be то же, что и предыдущая функция, но требуется поиск элемента через функции
# поиска
#
# alert_is_present  ожидание всплывающего окна на странице браузера
#
# element_to_be_clickable ожидание активности элемента
#
# Неявное ожидание
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://http://random.dinamic")
SomeDynamicElement = driver.find_element(By.ID, "SomeDynamicElement")


# Ожидание
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://random.dinamic")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(By.ID, "SomeDynamicElement"))
#
# Ожидаемые условия
# presence_of_all_elements_located ожидание присутствия в документе всех элементов, найденных с помощью указанного
# локатора
#
# pip freeze > requirements.txt

#
# Практика:
# 1. Множественным выбором убедитесь в количестве ваших питомцев
# 2. В выпадающем списке выберите любую категорию и напишите скрипт
# 3. Добавьте к своему скрипту фикстуру на открытие и закрытие в отдельно созданном файле
