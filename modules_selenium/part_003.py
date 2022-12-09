# coding: utf8
""" 
@File: part_003.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/9 4:51
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver.FirefoxOptions().binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' 
driver = webdriver.Firefox(executable_path=r'./driver/firefox_107_0_1_x86_64/win/geckodriver.exe')
driver.get('https://baidu.com')
time.sleep(2)
driver.find_element(by=By.ID, value='kw').send_keys('python')
time.sleep(3)
driver.find_element(by=By.ID, value='su').click()
time.sleep(3)
print(driver.title)
driver.quit()

