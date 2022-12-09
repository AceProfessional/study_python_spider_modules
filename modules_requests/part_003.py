# coding: utf8
""" 
@File: part_003.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/17 16:10
"""

import os, sys

"""在headers参数中携带cookie"""

import requests
from requests import utils

"""github示例"""

url = 'https://github.com/AliceEngineerPro'
# url = 'https://github.com/{USERNAME}'

# 构造请求头字典
headers = {
    # 从浏览器中复制过来的User-Agent
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    # 从浏览器中复制过来的Cookie
    # 'Cookie': 'cookie字符串'
}

# 请求头参数字典中携带cookie字符串
# response = requests.get(url, headers=headers, proxies={'http': 'http://127.0.0.1:56789'})
# print(response.content.decode())

"""cookies参数的使用"""

# 构建cookie字典 -> 字典推导式
cookie_temp = 'cookie字符串(cookies values)'

# 普通方法
# cookie_temp_list = cookie_temp.split('; ')
# cookies = {}
# for cookie in cookie_temp_list:
#     cookies[cookie.split('=')[0]]=cookie.split('=')[1]
"""
# 字典推导式
cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_temp.split('; ')}
response = requests.get(url=url, headers=headers, cookies=cookies, proxies={'http': 'http://127.0.0.1:56789', 'https': 'http://127.0.0.1:56789'})
with open(file='./data/save/github_with.html', mode='wb') as files:
    files.write(response.content)
files.close()
"""

"""RequestCookieJar对象转换为cookies字典的方法"""

url_baidu = 'https://baidu.com'
response = requests.get(url=url)
print(requests.utils.dict_from_cookiejar(response.cookies))







