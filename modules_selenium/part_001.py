# coding: utf8
""" 
@File: part_001.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/9 3:29
"""

from selenium import webdriver

# 如果driver没有添加到了环境变量，则需要将driver的绝对路径赋值给executable_path参数
webdriver.FirefoxOptions().binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'./driver/firefox_107_0_1_x86_64/win/geckodriver.exe')
# 如果driver添加了环境变量则不需要设置executable_path
# driver = webdriver.Firefox()

# 向一个url发起请求
driver.get('https://baidu.com')

# 打印页面的标题
print(driver.title)

# 退出模拟浏览器, 不退出会有残留进程！
driver.quit()
