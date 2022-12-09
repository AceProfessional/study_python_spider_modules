# coding: utf8
""" 
@File: part_006.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/9 9:24
"""

from selenium import webdriver
import time

webdriver.FirefoxOptions().binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
executable_path = r'./driver/firefox_107_0_1_x86_64/win/geckodriver.exe'
driver = webdriver.Firefox(executable_path=executable_path)
driver.get(url='https://baidu.com')
js_opentable = 'window.open("https://taobao.com")'
driver.execute_script(js_opentable)
time.sleep(2)
# 浏览器标签句柄
browser_windows = driver.window_handles
driver.switch_to.window(browser_windows[0])
time.sleep(5)
driver.switch_to.window(browser_windows[1])
time.sleep(5)
driver.quit()

