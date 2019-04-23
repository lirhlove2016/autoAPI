# coding:utf-8
from common import Http2 as Http
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
desfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\debug\autoTestApi_demo\datadir\myHttp_456.xls"


print(srcfile,desfile)
ex= ExcelUtil(srcfile)
data,key=ex.dict_data()

print(key)
wb=ex.copy_open(srcfile,desfile)

'''
data[3]["result"]="PASS"
data[3]["realresult"]="这个是 结果"
data[4]["result"]="Fail"

print(data[3]["result"])

ex.write_excel(wb,data,key,desfile)

'''


for i in range(3,len(data)):
    print(data)
    keyword=data[i]['keyword']
    arg1=data[i]['arg1']
    arg2=data[i]['arg2']
    arg3=data[i]['arg3']
    
    print("-------------------------------------------------------")


    if keyword=='post':
            datas=Http.api_request('post',arg1,arg2)

    elif keyword=='get':
            datas=Http.api_request('get',arg1,arg2)

    elif keyword=='put':
            datas=Http.api_request('put',arg1,arg2)

    elif keyword=='addheader':
            datas=Http.add_header(arg1,arg2)

    elif keyword=='assertequals':
            datas=Http.assert_equals(arg1,arg2)

    elif keyword=='savejson':
            datas=Http.saveJson(arg1,arg2)

    elif  keyword=='seturl':
            datas=Http.seturl(arg1)

    elif  keyword=='settimeout':
            datas=Http.settimeout(arg1)

    elif  keyword=='addparam':
            datas=Http.add_param(arg1,arg2)

    elif  keyword=='removeheader':
            datas=Http.remove_header(arg1)
        
    else:
        datas=""
        print('keyword not exist.')

    if len(datas)>1:
        data[i]['result']=datas[0]
        data[i]['realresult']=datas[1]

ex.write_excel(wb,data,key,desfile)
    
    
    

