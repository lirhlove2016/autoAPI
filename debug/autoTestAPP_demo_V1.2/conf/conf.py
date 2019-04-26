#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
version=1.0

'''
by lirh
'''
#设置目录
filepath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dataDir=os.path.join(filepath,'datadir')
reportDir=os.path.join(filepath,'report')
pageDir = os.path.join(filepath, 'report/pages/')
imageDir = os.path.join(filepath, 'report/image/')  #截图
logDir = os.path.join(filepath, 'report/logs/')  #log
htmlDir = os.path.join(filepath, 'report/html/')  #log
#设置包名
appPackage=""
appActivity=""

#uninstall
uninstallPackage=""
#const常量 替换id中包名
PACK="com.aikan"

#弹窗关闭id
tanchuang_close_id=["%s:id/imageview_close"%PACK,"%s:id/imageview_cloud_sysch_close"%PACK]



if __name__=="__main__":
    print(dataDir)
    print(reportDir)
    
