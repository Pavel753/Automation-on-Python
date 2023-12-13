import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://34.141.58.52:8080/#/'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.ID, 'pv_id_2').click()
    time.sleep(1)
    browser.find_element(By.ID, 'pv_id_2_1').click()
    time.sleep(1)

    browser.save_screenshot('result2.png')

finally:
    browser.quit()
