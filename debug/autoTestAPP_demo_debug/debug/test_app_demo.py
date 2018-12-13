# coding:utf-8
from common import elementApp as app
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
import re
import time

#配置data文件目录
filepath=r"E:\myworkspace\mygit\autoTestAPP_demo\datadir"
srcfile=filepath+"\myApp.xls"
desfile=filepath+"\myApp_result.xls"
resultfile=filepath+"\result\screenshot\screenshot_"


def run(line):
        if line[3]=='caps':
            app.update_capability(line[4],line[5])
            return
        if line[3]=='start':
            app.start(line[4],line[5])
            return
        if line[3]=='sleep':
            app.sleep(line[4])
            return
        if line[3]=='swip':
            app.swip(line[4],line[5])
            return
        if line[3]=='id':
            app.get_element("id",line[4],line[5],line[6])
            return
        if line[3]=='name':
            app.get_element("name",line[4],line[5],line[6])
            return
        if line[3]=='text':
            app.get_element("text",line[4],line[5],line[6])
            return
        if line[3]=='css':
            app.get_element("css",line[4],line[5],line[6])
            return
        if line[3]=='xpath':
            app.get_element("xpath",line[4],line[5],line[6])
            return
        if line[3]=='class':
            app.get_element("class",line[4],line[5],line[6])
            return     
        if line[3]=='click':
            app.clicks("click",line[4],line[5],line[6])
            return
        if line[3]=='clear':
            app.clicks("clear",line[4],line[5],line[6])
            return
        if line[3]=='input':
            app.clicks("input",line[4],line[5],line[6])
            return    

        if  line[3]=='assertequals':
            app.assertequals(line[4],line[5])
            return
        if  line[3]=='savephoto':
            app.get_screenshot(resultfile,line[4])
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


