# coding:utf-8
from common import Http
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
import re
import os
#srcfile=r"E:\autoTestApi\datadir\myHttp.xls"
#desfile=r"E:\autoTestApi\datadir\myHttp123_result.xls"
filepath=os.path.abspath(os.getcwd())
#print(filepath)
srcfile=os.path.join(filepath,'datadir/myHttp.xls')
desfile=os.path.join(filepath,'datadir/myHttp_result.xls')

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
num=1
for i in range(1,reader.r):
    line=reader.readline()
    #print(line)
    if len(line[0])>2 or len(line[1])>2:
        #不去执行的行
        pass
    else:
        #执行
        print(line)        
        print('正在执行第%s个-----------------------------------'%num) 
        run(line)
        num=num+1
       
                                                        
writer.save_close()


