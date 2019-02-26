#coding:utf-8
from appium import webdriver
import time,os

import getxml  as xmlfile
import common
from appium.webdriver.common.touch_action import TouchAction 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

from clicks import *



print('正在启动客户端.....')
time.sleep(5)
print('打开客户端了')

print('启动页滑动...')

#启动页向左滑动
i=0
while i <3:
    swipeLeft()
    i=i+1

print('已经滑动到第3页，正在选择男 女 ...')
driver.find_element_by_id("com.ishugui:id/tv_man").click()

print('您选择了 “男生小说”')

tanchuang_closseid=["com.ishugui:id/imageview_close","com.ishugui:id/imageview_cloud_sysch_close"]

#进入主界面，判断弹窗
huodong="com.ishugui:id/imageview_close"
tanchuang(huodong)

id="com.ishugui:id/imageview_cloud_sysch_close"
tanchuang(id)

#单次执行
#书架
print('正在执行书架操作-------------------------------')
shujia="com.ishugui:id/imageView"
click_all(shujia,'id')
print('点击了书架')
name="shujia"
ac=get_current_activity()
print(ac)
#取source，进行操作
#getsource_clicks(name)

#书城
print('正在执行书城操作-------------------------------')
shucheng="书城"
name="shucheng"
click_all("书城",'text')
print('点击了书城')
ac=get_current_activity()
print(ac)

#取source，进行操作
getsource_clicks(name)

'''
#我的
click_all("我的",'text')
ac=get_current_activity()
print(ac)

#分类
name="fenlei"
click_all("分类",'text')
ac=get_current_activity()
print(ac)
'''

'''
#多次执行

#执行页面数统计
num=1
time.sleep(3)
level=1  #跳转几层
#获取当前页面pagesource
r=get_pagesource()
#ac = get_current_activity(driver)
#存储文件名
filename="page_%s.xml"%num
re=source_clicks(r,filename)
#有返回，执行返回操作，进入一个新页

if re:
    num=num+1
    filename="page_%s.xml"%num
    for i in range(len(result)):
        if id in result[i].keys():
            value=result[i].value()
            clickid(value)
            #获取当前页面pagesource
            r=get_pagesource()          
            source_clicks(r,filename)


#2
time.sleep(3)
#获取当前页面pagesource
r=get_pagesource()
#ac = get_current_activity(driver)
#存储文件名
filename="page_%s.xml"%num
re=source_clicks(r,filename)
#有返回，执行返回操作，进入一个新页
if re:
    num=num+1
    filename="page_%s.xml"%num
    for i in range(len(result)):
        if id in result[i].keys():
            value=result[i].value()
            clickid(value)
            r=get_pagesource()          
            source_clicks(r,filename)




#2
time.sleep(3)
#获取当前页面pagesource
r=get_pagesource()
#ac = get_current_activity(driver)
#存储文件名
filename="page_%s.xml"%num
re=source_clicks(r,filename)
#有返回，执行返回操作，进入一个新页

if re:
    num=num+1
    filename="page_%s.xml"%num
    for i in range(len(result)):
        if id in result[i].keys():
            value=result[i].value()
            clickid(value)
            #获取当前页面pagesource
            r=get_pagesource()          
            source_clicks(r,filename)


'''

