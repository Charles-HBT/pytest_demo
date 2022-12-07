import yaml
import configparser
from common.logger import logger
import json
import xlrd

class ReadFileData():
    def __init__(self):
        pass

    def load_yaml(self,file_path):
        logger.info("加载{} 文件....".format(file_path))
        with open(file_path,encoding='utf-8') as f:
            data=yaml.safe_load(f)
        logger.info("读到数据==> {}".format(data))
        return data

    def load_json(self,file_path):
        logger.info("加载{} 文件....".format(file_path))
        with open(file_path,encoding='utf-8') as f:
            data=json.load(f)
        logger.info("读到数据==> {}".format(data))
        return data

    def load_ini(self,file_path):
        logger.info("加载{} 文件....".format(file_path))
        config=configparser.ConfigParser()
        config.read(file_path,encoding='utf-8')
        data=config._sections #以字典的形式返回配置文件中所有内容
        logger.info("读到数据==> {}".format(data))
        return data

    def load_excel(self,file_path):
        logger.info("加载{} 文件....".format(file_path))
        fb = xlrd.open_workbook(file_path)
        sheetnames = fb.sheet_names()
        # print(sheetnames)
        casesheet = fb.sheet_by_index(0) #根据sheet的索引获取sheet
        rows = casesheet.nrows
        data= []
        for row in range(1, rows):
            data.append(casesheet.row_values(row))
        logger.info("读到数据==> {}".format(data))
        return data

# data=ReadFileData()