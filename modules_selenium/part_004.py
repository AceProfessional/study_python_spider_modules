# coding: utf8
""" 
@File: part_004.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/9 6:33
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://baidu.com/'
driver_path = r'./driver/firefox_107_0_1_x86_64/win/geckodriver.exe'
webdriver.FirefoxOptions().binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get(url=url)
print(driver.page_source)
driver.find_element(by=By.ID, value='kw').send_keys('python')
driver.find_element(by=By.ID, value='su').click()
time.sleep(3)
driver.save_screenshot(filename='./python_百度搜索.png')
print(driver.current_url)
driver.get(url='https://douban.com/')
driver.save_screenshot(filename='./豆瓣主页.png')
driver.back()
driver.forward()
time.sleep(3)
driver.quit()


