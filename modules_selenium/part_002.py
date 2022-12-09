# coding: utf8
""" 
@File: part_002.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/9 3:32
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument(argument='-headless')
options.add_argument(argument='--disable-gpu')
driver = webdriver.Firefox(executable_path=r'./driver/firefox_107_0_1_x86_64/win/geckodriver.exe', options=options)
driver.get(url=r'https://baidu.com')
# print(driver.page_source)
driver.save_screenshot('./1.png')
driver.quit()
