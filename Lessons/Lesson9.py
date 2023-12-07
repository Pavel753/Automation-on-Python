# Локаторы ID
# Локаторы Name
# Локаторы ClassName
# Локаторы CSS
# Локаторы XPath


# $$("CSS-локатор") — ищет все элементы в DOM по данному CSS-селектору.
#
# аналог: document.querySelectorAll("CSS-локатор")
# для возвращения только первого найденного элемента:
#
# document.querySelector("CSS-локатор")


# Пример 1: $x('//a[contains(text(), "Students")]')
# Находит все теги ссылок, внутри которых есть текст "Students".
# Пример 2: $x('//div[contains(@class, "p-inputtext p-component")]')
# Находит все div у которых в имени класса есть строчка "p-inputtext p-component".
# Пример 3: $x('//img[contains(@src, ".jpg")]')
# Находит все jpg-картинки.


# CSS-локатор — document.querySelectorAll("css") или $$("css")
#
#
# точка (.) ставится перед именем класса
# решетка (#) — перед идентификатором
# пробел — перед спуском «вниз»
# XPath-локатор — $x('//x[@path]')
#
#
# звёздочка(*) означает произвольный тег
# квадратные скобки — [ ] — обращение к атрибутам тега

# Поиск id $x('//*[@id]')

# Полезные ссылки:
# CSS Selector Справочник: https://html5css.ru/cssref/css_selectors.php
# Использование CSS (на английском языке): https://www.softwaretestinghelp.com/css-selector-selenium-locator-selenium-tutorial-6/
# Изучаем xpath: https://msiter.ru/tutorials/xpath
# XPath in Selenium: How to Find & Write Text, Contains, OR, AND: https://www.guru99.com/xpath-selenium.html#1
# Полезные шаблоны: https://devhints.io/xpath
# Типы локаторов: https://comaqa.gitbook.io/selenium-webdriver-lectures/selenium-webdriver.-vvedenie/tipy-lokatorov
# Локаторы css, xpath: https://comaqa.gitbook.io/selenium-webdriver-lectures/selenium-webdriver.-slozhnye-voprosy./lokatory.-css-xpath-jquery.
# Выбираем локаторы: https://automated-testing.info/t/selenium-znakomimsya-s-lokatorami-i-vybiraem-pravilnyj/2268
