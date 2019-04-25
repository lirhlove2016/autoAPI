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

#设置包名
appPackage=""
appActivity=""

#uninstall
uninstallPackage=""

package="com.ishugui"
#弹窗关闭id
tanchuang_close_id=["%s:id/imageview_close"%package,"%s:id/imageview_cloud_sysch_close"%package]


if __name__=="__main__":
    print(dataDir)
    print(reportDir)
    
