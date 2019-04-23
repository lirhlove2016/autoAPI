#coding=utf-8
import time
import os
import re
import sys
"""
1.get_app_deviceid
2.get_app_activity_and_packagename

"""

#------------------------------------------------------
#下面的代码是获取当前窗口的component参数
def getFocusedPackageAndActivity():
 
		pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+") #这里使用了正则表达式，对输出的内容做了限制，只会显示类似"com.mediatek.factorymode/com.mediatek.factorymode.FactoryMode"的字符串
		out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read()  #window下使用findstr
		list = pattern.findall(out)
		print('list----',list)
		component = list[0]       #输出列表中的第一条字符串 
		return component	    
#print(getFocusedPackageAndActivity())
#------------------------------------------------------
#提取设备号
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
#获取包名和activity
def get_app_activity_and_packagename():
        '''实现提取设备号
           res=get_app_activity_and_packagename()
        '''    
        #正则表达式 输出包名
        pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")    
        out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read() #window下使用findstr
        out_list = pattern.findall(out)
        print('list----',out_list)
        component = out_list[0] #输出列表中的第一条字符串
        print(component)
        '''
        #方法1，提取pack,act
        pack = str(re.findall('name=(\w+(\.\w+){1,})',out,flags=0))
        pack=str(re.findall('\'(.+?)\',',pack,flags=0))
        activity = str(re.findall('/(\w+(\.\w+){1,})',out,flags=0))
        activity = str(re.findall('\'(.+?)\',',activity,flags=0))
        '''
        #方法2
        res=component.split('/')
        pack=res[0]        
        activity=res[1]
        print("package="+pack+'\n'+"activity="+activity)        

        return res
#------------------------------------------------------        
#安装app
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
        
        #os.system(cmd)
        

#卸载app
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
        
        #os.system(cmd)
                
#-------------------------------------
#app包目录获取
def get_app_filelist(strlj):
    global L
    L = []
    for aaa, bbb, ccc in os.walk(strlj):
        ccc = str(ccc)
        if ccc != '[]':
            ccc = ccc.split(',')
            ccc = list(ccc)
            n = 0
            for CCC in ccc:
                zz = ccc[n].replace("'", "")
                zz = zz.replace("]", "")
                zz = zz.replace("[", "")
                zz = zz.replace(" ", "")
                n = n + 1
                # print(os.path.join(aaa, zz))
                L.append(os.path.join(aaa, zz))
				
#示例如下，r是转义\
#get_app_filelist(r'D:\我的文档\app自动化\TESTfile')
#print(L)
#-------------------------------------
#目录下包安装方法，一个一个执行，还是隔几个执行，还是只安装几个





if  __name__=='__main__':

    ''' 
    os.system('adb version')
    os.system('adb devices')    #os.system是不支持读取操作的
    out = os.popen('adb shell "dumpsys activity | grep "mFocusedActivity""').read() #os.popen支持读取操作
    print(out)
    '''    
    #print(getFocusedPackageAndActivity())
    #get_app_deviceid()
    res=get_app_activity_and_packagename()
    print(res)              

    apppath="F:\\download\\397aikan.apk"
    
    install_appPackage(apppath)
    time.sleep(5)
    packname='com.ishugui'
    uninstall_apppackage(packname)

    



