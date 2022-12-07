# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import requests
import json
import pytest
import allure
from common.read_data import *
from common.logger import logger
from base.method import ApiRequest
from common.get_path import return_path
import os

root_path=return_path()
data_path=os.path.join(root_path,'data\\123.xls')
url_path=os.path.join(root_path,'config\\setting.ini')
data=ReadFileData().load_excel(data_path)

@pytest.mark.parametrize('description,method,headers,params,expect',data)
def test_api(description,method,headers,params,expect):
    logger.info("执行测试用例{}".format(description))
    logger.info("测试用例方法{}".format(method))
    logger.info("测试用例请求头{}".format(headers))
    logger.info("测试用例请求参数{}".format(params))
    logger.info("测试用例预期{}".format(expect))
    url=ReadFileData().load_ini(url_path)['host']['api_url']
    if method=='GET':
         response=ApiRequest().send_requests(
             method=method,
             url=url,
             data=params)
         status=response.status_code
         assert status==200
    elif method=='POST':
        response=ApiRequest().send_requests(
            method=method,
            url=url,
            data=json.loads(params)
        )
        status = response.status_code
        assert status == 200
