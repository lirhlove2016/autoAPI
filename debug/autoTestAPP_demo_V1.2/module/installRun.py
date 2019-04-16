#!/usr/bin/env python
#coding=utf-8

import os
import platform
import subprocess
import re
from time import sleep
from common.appInstallCommon import *

"""
运行安装app包
1.设置包目录
2.配置安装模式，0顺序，N跳着，-1比例
3.卸载包
"""

#----------------设备包目录----------------------
#app包所在目录
appFilepath="F:\\04.03" 
#----------------配置安装模式--------------------
#安装参数0,顺序安装，-1为按比例安装，正整数跳着安装
method=0   
radio=0.3
#包名
pack="com.ishugui"

#设置从第几个开始执行安装，当大于1时从设置数开始进行安装
startnum=1
#---------------参数配置  end--------------------

#----------------执行操作-------------------------
print('包所在目录为：',appFilepath)
#appfiles=get_app_filelist(r'F:\download')
appfiles=get_app_filelist(appFilepath)
#print(appfiles)
for x in appfiles:
    print(x)
print()

#从第几个包开始安装
if startnum>1:
    temp=appfiles[startnum-1:]
    print('安装包：--------------------------------------------')
    for x in temp:
        print(x)
    appfiles=temp
    
#文件夹安装
install_app_run(appfiles,method,radio=0.3)

#----------------执行操作-------------------------
