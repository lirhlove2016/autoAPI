# coding:utf-8
from common import elementApp as app
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
import re
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.conf import *



#-文件目录配置----------------------------

#2.配置data文件目录,取当前目录
#filepath=r"E:\download"
#filepath=os.path.abspath(os.getcwd())
srcfile=os.path.join(filepath,'datadir/myApp.xls')
desfile=os.path.join(filepath,'datadir/myApp_result.xls')
resultfile=os.path.join(filepath,'result/screenshot/screenshot_')


#conf配置
srcfile=os.path.join(dataDir,'myApp.xls')
desfile=os.path.join(dataDir,'myApp_result.xls')
resultfile=os.path.join(reportDir,'screenshot/screenshot_')
print(dataDir,srcfile)



#-脚本-----------------------------------
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

        if line[3]=='right':
            #app.RIGHT()
            app.swiptest("right",line[4])
            return
        if line[3]=='left':
            #app.LEFT()
            app.swiptest("left",line[4])
            return
        if line[3]=='up':
            #app.UP()
            app.swiptest("up",line[4])
            return
        if line[3]=='down':
            #app.DOWN()
            app.swiptest("down",line[4])                
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

        if  line[3]=='quit':
            app.quit()
            return

        if  line[3]=='back':
            app.back()
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
print('执行完成---------------')

#----end------------------------------------------
