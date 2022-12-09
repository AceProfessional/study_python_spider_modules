# coding: utf8
""" 
@File: part_007.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/9 10:30
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

url = 'https://mail.qq.com/cgi-bin/loginpage'
driver.get(url)
time.sleep(2)

login_frame = driver.find_element(by=By.ID, value='login_frame') # 根据id定位 frame元素
driver.switch_to.frame(login_frame) # 转向到该frame中
driver.find_element(by=By.XPATH, value='//*[@id="u"]').send_keys('1596930226@qq.com')
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="p"]').send_keys('hahamimashicuode')
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="login_button"]').click()
time.sleep(2)
# 操作frame外边的元素需要切换出去
windows = driver.window_handles
driver.switch_to.window(windows[0])
content = driver.find_element(by=By.CLASS_NAME, value='login_pictures_title').text
print(content)
driver.quit()
