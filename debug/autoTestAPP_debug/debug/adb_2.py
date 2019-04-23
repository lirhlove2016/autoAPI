import time
import os
import re
import sys
 

os.system('adb version')
os.system('adb devices')    #os.system是不支持读取操作的
out = os.popen('adb shell "dumpsys activity | grep "mFocusedActivity""').read() #os.popen支持读取操作
print(out)


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
    #
    patter= re.compile(r"[a-zA-Z0-9]+") 
    device_list=patter.findall(out)
    #print(device_list)
    print('设备连接信息:--------------------------------------\n',out)
    #存放设备号
    deviceid=[]

    devices_array=[]
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

#get_app_deviceid()
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
        pack = str(re.findall('name=(\w+(\.\w+){1,})',out,flags=0))
        pack=str(re.findall('\'(.+?)\',',pack,flags=0))
        activity = str(re.findall('/(\w+(\.\w+){1,})',out,flags=0))
        activity = str(re.findall('\'(.+?)\',',activity,flags=0))
        '''    
        res=component.split('/')
        pack=res[0]        
        activity=res[1]
        print("package="+pack+'\n'+"activity="+activity)        

        return res

        
res=get_app_activity_and_packagename()
print(res)

               
#------------------------------------------------------
s=re.split('hello', 'hello world  hello') 
#print(s)


