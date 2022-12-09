# coding: utf8
""" 
@File: part_001.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/17 2:25
"""

import os, sys

"""初识requests模块和简单的response对象"""

import requests

url = 'https://baidu.com'
response = requests.get(url=url)
# print(response.text)
# print(response.content.decode())
print(response.content.decode('utf-8'))
# 响应的url
print('响应的url', response.url)
# 响应的状态码
print('响应的状态码', response.status_code)
# 响应对象的请求头
print('响应对象的请求头', response.request.headers)
# 响应头
print('响应头', response.headers)
# 请求携带的cookies(私有属性)
print('请求携带的cookies', response.request._cookies)
# 响应中携带的cookies
print('响应中携带的cookies', response.cookies)


