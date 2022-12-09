# coding: utf8
""" 
@File: part_005.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/9 7:08
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://movie.douban.com/explore'
driver_path = r'./driver/firefox_107_0_1_x86_64/win/geckodriver.exe'
webdriver.FirefoxOptions().binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get(url=url)
time.sleep(3)
ul = driver.find_elements(by=By.CLASS_NAME, value='explore-list')
for data in ul:
    for i in data.find_elements(by=By.TAG_NAME, value='a'):
        print(i.get_attribute('href'))
    for i in data.find_elements(by=By.CLASS_NAME, value='drc-subject-info-title-text'):
        print(i.text)
driver.quit()
