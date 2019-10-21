#coding=utf-8
import re
import os


"""
系统版本号，设备号，设备名称等
"""
#一个设备
'''
deviceName = os.popen('adb shell getprop ro.product.model').read() 
print(deviceName) 
platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
print(platformVersion) 
producter = os.popen('adb shell getprop ro.product.brand ').read() 
print(producter)
'''

##获取设备多台设备号列表
def get_deviceid():
    str_init=' '
    all_info= os.popen('adb devices').readlines()
    print('adb devices 输出的内容是：',all_info)

    for i in range(len(all_info)):
        str_init+=all_info[i]
    devices_name=re.findall('\n(.+?)\t',str_init,re.S)

    print('所有设备名称：\n',devices_name)
    return devices_name

r=get_deviceid()
#print(r)

