# coding: utf8
""" 
@File: part_002.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/17 15:26
"""

import os, sys

"""requests发送请求"""

import requests

url = 'https://baidu.com'
response = requests.get(url=url)
# print(response.content.decode())
# 打印响应对应请求的请求头信息
print(response.request.headers)
print(f'没有自定义headers返回的响应头大小: {len(response.content.decode())}')

"""发送带headers的请求"""

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 在请求头中带上User-Agent, 模拟浏览器发送请求
response = requests.get(url=url, headers=headers)
# 打印请求头
print(response.request.headers)
print(f'自定义headers返回的响应头大小: {len(response.content.decode())}')

"""发送带参数的请求"""

url = 'https://baidu.com/s'
# url = 'https://baidu.com/s?wd=python'
# response = requests.get(url=url, headers=headers)

# 请求参数是一个字典 即wd=python
params = {
    'wd': 'python'
}
# 带上请求参数发起请求，获取响应
response = requests.get(url=url, headers=headers, params=params)

