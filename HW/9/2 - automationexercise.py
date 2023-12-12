import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://automationexercise.com/'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    button.click()

    input1 = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
    input1.send_keys('Pavel')

    input2 = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
    input2.send_keys('Pif_753@mail.ru')

    button1 = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
    button1.submit()

    button2 = browser.find_element(By.ID, 'id_gender1')
    button2.click()

    time.sleep(5)
    browser.save_screenshot('result2.png')

finally:
    browser.quit()
