# coding: utf8
""" 
@File: part_009.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/11 9:15
"""

from selenium import webdriver
import time

webdriver.FirefoxOptions().binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
executable_path = r'./driver/firefox_107_0_1_x86_64/win/geckodriver.exe'
driver = webdriver.Firefox(executable_path=executable_path)
driver.get(url='https://qq.com')
js = '''window.scrollTo(0,document.body.scrollHeight)'''
driver.execute_script(script=js)
time.sleep(5)
driver.quit()
