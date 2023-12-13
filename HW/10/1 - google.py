import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1200, 800)
driver.get('https://www.google.com/')

time.sleep(5)

serch_box = driver.find_element(By.NAME, 'q')
serch_box.send_keys('QaLearning')
serch_box.submit()

time.sleep(5)

driver.save_screenshot('result1.png')

driver.quit()
