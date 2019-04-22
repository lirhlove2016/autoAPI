#coding:utf-8
from appium import webdriver
import time
import os
from appium.webdriver.common.touch_action import TouchAction 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException

#TouchAction(driver).press(el0).moveTo(el1).release()

import module.getxml  as xmlfile
from conf.conf import *
"""
function:
1.xml存到文件，write_xml_to_file(filename,content)
2.从xml文件中获取值，getAttrib(filename,attriname)
3.从xml文件中取所有值，getAttrib_of_all(filename)
4.取页面Source，get_current_activity(driver)
5.

"""


#-----------------------------------------------------------
#xml 存到文件中
def write_xml_to_file(filename,content):
	with open(filename,"w+",encoding='utf-8') as f:
		f.write(content)
		print("写入xml到文件")
	
#-----------------------------------------------------------
#从xml文件，#根据class属性取值，如，android.widget.TextView
def  getAttrib(filename,attriname):
    R= xmlfile.getXmlNode(filename)
    t=[]
    #提取不同分类
    for x in R: 
        #print(x)
        if x[2]==attriname:
            t.append(x)
    return t   


#-----------------------------------------------------------
#从xml文件，取同一个属性的值先取text属性，存到name中，无text取resource-id,存到resourceid中
def  getAttrib_of_all(filename):
    R= xmlfile.getXmlNode(filename)
    #print(R)
    #存储所有属性
    name=[]
    ids=[]
    c=[]
    #只存name,id,class
    name_array=[]
    ids_array=[]
    c_array=[]
    print('正在取属性---------------------','共%d个属性'%(len(R)-1))

    #提取不同分类,从1开始，
    for i in range(1,len(R)):
        #取text，resource-id
        #print('正在取属性---------------------',i)
        #print(R[i])
        #text，id,class,clickable值    
        text=R[i][3]["text"]
        id=R[i][3]["resource-id"]
        class_value=R[i][3]["class"]
        clickable_value=R[i][3]["clickable"]

        #print(class_value,clickable_value)        
        #print(id)
        #是否是可点击的,true是可以点击的，进行存储，false，不存储      
        if clickable_value=="false":
                if class_value not in include:
                        #print('不可点 不存')
                        continue

        #如果是排除的属性，不存储                
        if class_value in  exclude:
                #print('class exclude 不存')
                continue
        
        #如果text 不为空，存到name中，id不为空存到resourceid中，否则存到c中
        if text!="":
                #name存所有属性，name_array只存在一个name值
                name.append(R[i])
                name_array.append(R[i][3]['text'])
                #print('存到name中')
                
        elif id!="":
                ids.append(R[i])
                ids_array.append(R[i][3]["resource-id"])
                #print('存到id中')
                
        else:
                c.append(R[i])
                c_array.append(R[i][3]["class"])
 
    '''
    #打印所有属性
    for i  in range(len(name)):
            class_value=name[i][3]["class"]
            clickable_value=name[i][3]["clickable"]
            print(i,class_value,clickable_value)
    '''
    #print(name[0][3])
           
    print("取值个数:",len(name),len(ids),len(c))
    #返回的所有属性   
    return name,ids,c
    #仅返回一个值
    #return name_array,ids_array,c_array
 
 #[13, 12, 'android.widget.TextView', {'selected': 'false', 'content-desc': '', 'enabled': 'true', 'checkable': 'false', 'checked': 'false', 'focusable': 'false', 'resource-id': 'com.aikan:id/tv_top_title_title', 'long-clickable': 'false', 'password': 'false', 'bounds': '[48,133][226,190]', 'focused': 'false', 'text': '本周已读 ', 'instance': '0', 'package': 'com.aikan', 'index': '0', 'clickable': 'false', 'scrollable': 'false', 'class': 'android.widget.TextView'}]
#-----------------------------------------------------------
# 获取当前界面activity
def get_current_activity(driver):
	ac = driver.current_activity
	print('当前的activity:----------------',ac)
	return ac

#-----------------------------------------------------------
def tap(x,y):
	adb = 'adb shell input tap %s %s'%(x,y)
	os.system(adb)

'''
#----------------------------------------------------------
#连续滑动两次设置手势press（）-按压release()-释放perform()-连续操作
for i in range(2): 
	TouchAction(driver).press(x=212,y=290).wait(2000)\
	.move_to(x=357,y=290).wait(5000)\
	.move_to(x=509,y=438).wait(1000)\
	.move_to(x=509,y=589).wait(1000)\
	.release().perform()
'''
#----------------------------------------------------------
#置后台x秒后再运行
def  background(driver,time):
	driver.background_app(time) 

#----------------------------------------------------------
#打系统通知栏（仅支持API 18 以上的安卓系统）
def notifications(driver):
        driver.open_notifications()   

#------------------------------------------------------------
def switch_h5(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.weizq"})


def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
#------------------------------------------------------------

if __name__=='__main__':

	filename="d:\\shujia.xml"	
	t=getAttrib(filename,"android.widget.TextView")
	#print(t)
	adb = 'adb devices'
	os.system('adb devices')
	
	


