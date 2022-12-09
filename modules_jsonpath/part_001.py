# coding: utf8
"""
@File: part_001.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/30 18:42
"""

from jsonpath import jsonpath

eg_dict = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': {'key7': {'key8': 'value'}}}}}}}}
print(eg_dict.get('key1').get('key2').get('key3').get('key4').get('key5').get('key6').get('key7').get('key8'))

print(jsonpath(eg_dict, '$..key8')[0])
