# -*- coding: utf-8 -*-
import xlrd

fb=xlrd.open_workbook("E:\谷歌浏览器下载\\api_auto_test-master\\testdata\\123.xls")
sheetnames=fb.sheet_names()
print(sheetnames)
casesheet=fb.sheet_by_name('Sheet1')
rows=casesheet.nrows
datalist=[]
for row in range(1,rows):
    # caselist=[]
    #读取测试文件中得五部分作为测试数据
#     url=casesheet.cell_value(row,1)
#     method=casesheet.cell_value(row,2)
#     header=casesheet.cell_value(row,3)
#     body=casesheet.cell_value(row,4)
#     expect=casesheet.cell_value(row,5)
#     # print(url,method,header,body,expect)
#     caselist.append(url)
#     caselist.append(method)
#     caselist.append(header)
#     caselist.append(body)
#     caselist.append(expect)
#     datalist.append(caselist)
# print(datalist)
    datalist.append(casesheet.row_values(row))
print(datalist)