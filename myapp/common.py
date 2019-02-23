#coding:utf-8
from appium import webdriver
import time
import os
import getxml  as xmlfile
from appium.webdriver.common.touch_action import TouchAction 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException


#TouchAction(driver).press(el0).moveTo(el1).release()

#-----------------------------------------------------------
#xml 存到文件中
def write_xml_to_file(filename,content):
	with open(filename,"w+",encoding='utf-8') as f:
		f.write(content)
		print("写入xml到文件")
	
#-----------------------------------------------------------
#从xml文件，取同一个属性的值
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

	filename="d:\\fenlei_write.xml"	
	t=getAttrib(filename,"android.widget.TextView")
	#print(t)
	adb = 'adb devices'
	os.system('adb devices')
	
	


