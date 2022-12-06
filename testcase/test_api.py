# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import requests
import json
import pytest
import allure
from common.read_data import *



data=ReadFileData().load_excel("..\data\\123.xls")
# print(data)
@allure.feature("用户登录功能测试")
@allure.story("get和post请求")
@pytest.mark.parametrize(("description","method","header","args","expect"),data)
def test_api(description,method,header,args,expect):
    url=ReadFileData().load_ini('..\config\\setting.ini')['host']['api_url']
    # logger.info("开始执行用例{}".format(description))
    response=requests.request(method,url)
    status=response.status_code
    assert status==200
# import json
# data=ReadFileData().load_excel("..\data\\123.xls")
# a={'name': 'hbt','password': '123456'}
# b=dict(a)
# print(b)
# print(type(b))
# c=json.dumps(b,sort_keys=True, indent=4, separators=(',', ': '))
# print(type(c))
# print(c)