#!/usr/bin/env python
#coding=utf-8

import os
import platform
import subprocess
import re
from time import sleep

from getAppfilepath import *
from adbUtils import *
"""
1.install_app_run

"""

#-------------------------------------
def  install_app_run(applist,interval=0,radio=0.3):
    '''
    applist:app包目录
    interval：0每个包都安装，正整数为间隔1隔安装,负值按比例安装
    radio:默认30%安装
    '''
    #存放app包数量
    total=len(applist)
    #num为0，都安装
    if interval==0:   
        print('当前安装模式顺序安装') 
        for apppath in applist:
            print(apppath)
            #install_appPackage(apppath)        
            #运行安装
                       
    #num大于0，间隔安装
    elif interval>0:
        print('当前安装模式跳着安装') 
        i=0  #计数
        for x in  applist:    
            #运行安装
            apppath=applist[i]
            print(i)
            install_appPackage(apppath)
            i=i+interval
            if i <total:
                continue
            else:
                break        
  
  #负数,按radio取百分比安装
    else:  
        print('当前安装模式按%s安装'%(radio))    
        num=int(total*radio)
        print(total,num)
        #需安装的个数
        p=int(total/num)
        i=0  #计数
        for x in  applist:    
            #运行安装
            apppath=applist[i]
            print(i+1)
            install_appPackage(apppath)
            i=i+p
            if i <total:
                continue
            else:
                break


if  __name__=='__main__':
    '''
    #print(getFocusedPackageAndActivity())
    get_app_deviceid()

    res=get_app_activity_and_packagename()
    print(res)              

    apppath="F:\\download\\397aikan.apk"
    
    install_appPackage(apppath)
    #time.sleep(5)
    packname='com.ishugui'
    #uninstall_appPackage(packname)

    '''
    appfile=get_app_filelist(r'F:\download')
    print(appfile)
    #单个安装
    #install_appPackage(appfile[0])

    #文件夹安装
    install_app_run(appfile,interval=2,radio=0.3)





    



