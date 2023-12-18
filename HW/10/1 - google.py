import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1200, 800)
driver.get('https://www.google.com/')

time.sleep(5)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('QaLearning')
search_box.submit()

time.sleep(5)

driver.save_screenshot('result1.png')

driver.quit()
