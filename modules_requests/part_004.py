# coding: utf8
""" 
@File: part_004.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/18 2:47
"""

import os, sys

"""超时timeout参数和proxies的使用"""

import requests

url = 'https://twitter.com'

try:
    response = requests.get(url=url, timeout=3)
    print('第一次请求', response.status_code)
except Exception as error:
    print('第一次请求', error)
finally:
    proxy = {
        'http': 'http://127.0.0.1:56789',
        'https': 'http://127.0.0.1:56789',
    }
    try:
        response = requests.get(url=url, timeout=3, proxies=proxy)
        print('第二次请求', response.status_code)
    except Exception as error:
        print('第二次请求', error)

