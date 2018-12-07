# coding:utf-8
from common import Http
from common.excel import ExcelUtil
import json
import jsonpath
import re
import os


filepath=os.path.abspath(os.getcwd())
#print(filepath)
srcfile=os.path.join(filepath,'datadir/myHttp.xls')
desfile=os.path.join(filepath,'datadir/myHttp_result.xls')

srcfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\debug\autoTestApi_demo\datadir\myHttp.xls"
desfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\debug\autoTestApi_demo\datadir\myHttp_123.xls"


print(srcfile,desfile)
ex= ExcelUtil(srcfile)
data,key=ex.dict_data()
print(data[3],key)
print(key)
ex.copy_open(srcfile,desfile)

data[3]["执行状态"]="PASS"
data[4]["执行状态"]="Fail"
ex.write_excel(desfile,data,key)


