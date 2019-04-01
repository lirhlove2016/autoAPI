#!/usr/bin/env python
#coding=utf-8

import os
import platform
import subprocess
import re
from time import sleep



PATH = lambda p: os.path.abspath(p)
print(PATH)

"""
1.get_app_deviceid
2.get_app_activity_and_packagename
3.install_appPackage
4.uninstall_apppackage
5.
"""

#------------------------------------------------------
def getFocusedPackageAndActivity():
    '''获取当前页的包名和activity    ''' 
    pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+") #这里使用了正则表达式，对输出的内容做了限制，只会显示类似"com.mediatek.factorymode/com.mediatek.factorymode.FactoryMode"的字符串
    out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read()  #window下使用findstr
    list = pattern.findall(out)
    #print('list----',list)
    component = list[0]   #输出列表中的第一条字符串 
    return component	    

#------------------------------------------------------
def get_app_deviceid():
    '''实现提取设备号
       get_app_deviceid()
    '''
    print('请先检查是否连接了设备，是否启动了开发者选项，是否开启了adb调试....')
    #查看连接设备
    out=os.popen('adb devices').read()
    patter= re.compile(r"[a-zA-Z0-9]+") 
    device_list=patter.findall(out)
    #print(device_list)
    print('设备连接信息:--------------------------------------\n',out)
    #存放设备号
    deviceid=[]
    #提取设备号，存放到deviceid中，
    if 'device' in device_list:
        #print('设备号:',deviceid)
        #多个设备，
        n=4
        while len(device_list)>n:
            deviceid.append(device_list[n])
            n=n+2
        print('设备号:',deviceid)        
    else:
        print('无此设备，请检查是否连接设备。')
#------------------------------------------------------
def get_app_activity_and_packagename():
        '''实现提取设备号
           res=get_app_activity_and_packagename()
        '''    
        #正则表达式 输出包名
        pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")    
        out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read() #window下使用findstr
        out_list = pattern.findall(out)
        component = out_list[0] #输出列表中的第一条字符串
        #print(component)
        res=component.split('/')
        pack=res[0]        
        activity=res[1]
        print("package="+pack+'\n'+"activity="+activity)        
        return res
#------------------------------------------------------        
def install_appPackage(apppath):
        '''
        安装apppath下的app包      
        '''
        cmd='adb install %s'%apppath
        out = os.popen(cmd).read()

        if 'Success' in out:
            print('success，app包安装成功了！')
        else:
            print('安装失败，请检查是否连接设备，是否已经安装。')
#------------------------------------------------------        
def uninstall_apppackage(packname):
        '''
        卸载app包      
        '''
        cmd='adb uninstall %s'%packname
        out = os.popen(cmd).read()        
        if 'Success' in out:
            print('success，app包已经卸载了！')
        else:
            print('卸载失败，请检查是否连接设备。')
#------------------------------------------------------  
def adb(args):
    cmd = "%s %s %s" % (command,str(args),device_id)
    
    r=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return r

def getDeviceID():
    args="get-serialno"
    return adb("get-serialno").stdout.read().strip()
	
#------------------------------------------------------  

if  __name__=='__main__':
    '''
    #print(getFocusedPackageAndActivity())
    #get_app_deviceid()
    res=get_app_activity_and_packagename()
    print(res)              

    apppath="F:\\download\\397aikan.apk"
    
    #install_appPackage(apppath)
    #time.sleep(5)
    packname='com.ishugui'
    #uninstall_apppackage(packname)

    '''
    args="adb devices"    
    r=adb(args).stdout.read().strip()
    args="get-serialno"
    r=adb(args).stdout.read().strip()
    print(r)



    



