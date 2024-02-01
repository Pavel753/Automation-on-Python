# Pytest-BDD
#
#
# Фича: создание нового питомца                               Feature: Creating a new pet
# Сценарий: создать нового питомца                             Scenario: Create a new pet
# Если: я на странице профайла                                Given: I am on my profile page
# Когда: я создаю нового питомца                              When: I create a new pet
# Тогда: я должен увидеть созданного питомца в своем профайле  Then: I should see created pet in my profile
import pytest

Фича: авторизация в приложении
Сценарий: валидная авторизация
Если: я на странице авторизации
Когда: я авторизуюсь с валидными данными
Тогда: я должен перейти на страницу профиля

Фича: невалидная авторизация в приложении
Сценарий: невалидная авторизация
Если: я на странице авторизации
Когда: я авторизуюсь с невалидными данными
Тогда: я должен получить сообщение об ошибке


@pytest.fixture(autouse=True)
def browser():
    br = webdriver.Chrome()
    yield br
    br.quit()

@scenario('app_login.feature', "Valid_Login")
def test_valid_login():
    pass

@scenario('app_login.feature', "InValid_Login")
def test_invalid_login():
    pass

@given("I visit login page")
def visit_page(browser):
    browser.get("наша страница")

@when("I login with valid creds")
def


@then("")
def on_profile_page(browser):
    assert






# Gherkin
# В словарь языка включено десять ключевых слов (Given, When, Then, And, But, Scenario, Feature, Background,
#                                                Scenario Outline, Examples)

# CI (Continuous Integration) — непрерывная интеграция
#
# CD, (Continuous Delivery) — непрерывная поставка
#
# Continuous Deployment — непрерывное развёртывание
#
# Цели CI/CD:
# обеспечение последовательного и автоматизированного способа сборки, упаковки и тестирования;
# автоматизация развёртывания в разных окружениях;
# сведение к минимуму ошибок и проблем.
#
# Инструменты для   CI/CD:
# Jenkins/Gitlab CI/Travis CI/Github Actions
#
# Тестирование баз данных
# 1. Убедитесь, что у полей данных правильный тип
# 2. Убедитесь, что обязательные поля базы данных обязательны и в API, и в интерфейсе
# 3. Убедитесь, что параметры полей в базе данных соответствуют параметрам в API и UI
# 4. Убедитесь, что важные данные зашифрованы в БД
# 5. Убедитесь, что БД поддерживает все API-операции
# 6. Убедитесь, что ведущие и замыкающие пробелы удаляются при сохранении записи в БД

# В файле app_config.json описываем подключение к стендам и бд
# В файле db_queries.py описываем запросы к бд
