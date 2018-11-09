# coding:utf-8
from common import Http as Http
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
import re

#jsonpath.jsonpath(json,"$['store']['book'][0]['author']")

srcfile=r"D:\workdtation\mygitwork\autoAPI\autoTestApi\datadir\myapp_Http.xls"
desfile=r"D:\workdtation\mygitwork\autoAPI\autoTestApi\datadir\myapp_HTTP_result.xls"

def run(line):
    if line[3]=='post':
        Http.api_request('post',line[4],line[5])
        return
    if line[3]=='get':
        Http.api_request('get',line[4],line[5])
        return
    if line[3]=='put':
        Http.api_request('put',line[4],line[5])
        return
        return
    if line[3]=='delete':
        Http.api_request('delete',line[4],line[5])
        return
    if line[3]=='addheader':
        Http.add_header(line[4],line[5])
        return
    if line[3]=='assertequals':
        Http.assert_equals(line[4],line[5])
        return
    if line[3]=='savejson':
        Http.saveJson(line[4],line[5])
        return
    if  line[3]=='seturl':
        Http.seturl(line[4])
        return
    if  line[3]=='settimeout':
        Http.settimeout(line[4])
        return
    if  line[3]=='addparam':
        Http.add_param(line[4],line[5])
        return
    if  line[3]=='removeheader':
        Http.remove_header(line[4])
        return


reader.open_excel(srcfile)
writer.copy_open(srcfile,desfile)

for i in range(0,reader.r):
    line=reader.readline()
    print(line)
    if len(line[0])>2 or len(line[1])>2:
        #不去执行的行
        pass
    else:
        #执行
        run(line)
        pass
                                                        
writer.save_close()


