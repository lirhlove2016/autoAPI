#!/usr/bin/env python 
# -*- encoding: utf-8 -*-
import os 
import time 
from multiprocessing import Pool 
list=[] 

def getDevicesAll(): 
	#获取devices数量和名称 
	devices = [] 
	try: 
		for dName_ in os.popen("adb devices"): 
			if "\t" in dName_: 
				if dName_.find("emulator") < 0: 
					devices.append(dName_.split("\t")[0]) 
		devices.sort(cmp=None, key=None, reverse=False) 
		print(devices) 
	except: 
		pass 
	print(u"\n设备名称: %s \n总数量:%s台" % (devices, len(devices))) 
	return devices 

def quickinstall(device):
	packagename="com.ishugui"
	#卸载原有apk 
	try:

		os.system('adb -s ' + device + ' uninstall %s'%packagename)
		os.system('adb -s ' + device + ' uninstall %s'%packagename)
		print(device + " 卸载成功\n")
	except: 
		print(device + " 卸载失败\n")

	try:
		print('-----list-----',list)

		for i in list: 
			os.system('adb -s ' + device + ' install ' + i)

	except: 
		print(device + " 安装失败\n")
	print(device + " 安装成功\n")

def qainstall(devices,):
	starttime=time.time() 
	pool = Pool(2) #创建8个任务池
	result=pool.map(quickinstall,devices)
	endtime=time.time() 
	pool.close() 
	pool.join() 
	print(endtime-starttime) #打印时间 

def get_apk(filename):
	global  list
	#filesname = 'F:/download/apk'
	#获取安装包
	print(filesname)
	for parent, dirnames, filnames in os.walk(filesname):
		for filname in filnames:
			path = os.path.join(parent, filname)
			list.append(path)
	print('-----list-----', list)
	return  list

#包路径
filesname = 'F:/download/apk'
#获取安装包
print(filesname)
for parent, dirnames, filnames in os.walk(filesname):
	for filname in filnames:
		path = os.path.join(parent, filname)
		list.append(path)
print('-----list-----', list)


if __name__ == "__main__":

	filesname = 'F:/download/apk'
	list=get_apk(filesname)

	try:
		devices = getDevicesAll() 
	except: 
		print("获取设备出错") 
	res = input("输入1开始更新:") 

	if int(res) == 1: 
		try:
			qainstall(devices)
		except:
			print("更新失败")
	#Touch(devices)
