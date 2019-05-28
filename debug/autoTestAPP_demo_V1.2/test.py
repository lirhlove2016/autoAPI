# coding:utf-8
from common import elementApp as app
from common import readexcel as reader, writeexcel as writer

from appium.webdriver.common.touch_action import TouchAction
import time
import os
import random
from conf.conf import dataDir,reportDir,pageDir,imageDir
from common import elementApp as app
from module import pil_common as image


#定义你的设备信息
app.update_capability('platformName','Android')
app.update_capability('platformVersion','8.0.0')        #9
app.update_capability('deviceName','SNMBB18417516563')   #UYT0218209004285
app.update_capability('appPackage','com.ishugui')
app.update_capability('appActivity','com.dzbook.activity.LogoActivity')
app.update_capability('automationName','UiAutomator2')
app.update_capability('appActivity','com.dzbook.activity.LogoActivity')
app.update_capability('automationName','UiAutomator2')


#引用你要调试的文件中的driver
app.start('http://localhost:4723/wd/hub',30)
driver = app.driver

#获取
print('启动客户端.....')
app.sleep(1)
driver=app.driver
#点击男
print('已经滑动到第3页，正在选择男 女 ...')
app.get_element("id","com.ishugui:id/tv_man","","man",'selectman')
app.clicks("click","man")
print('选择男生，进入主界面')
app.sleep(1)

print("等待5秒")
app.step_insterval_time()

#保存图
number=3
app.get_screenshot(imageDir, "%s_%d.png" % ("shujia", number))
print("保存图片")

new = 'new UiSelector().textContains(\"' + "今日签到" + '\")'
el = driver.find_element_by_android_uiautomator(new)

t=el.get_attribute("bounds")
print("t--",t,type(t))


#定位元素，获取元素bounds,保存图片，
number=1
def  get_element_pic(casename,el):
    global number,driver
    filepath="./report/image/%s_%d.png"%(casename, number)
    get_screenshot(imageDir, "%s_%d.png" % (casename, number))
    print("保存图片")
    #
    # 获取坐标
    bounds = el.get_attribute("bounds")
    recxy = image.get_bounds_xy(bounds)
    print(recxy, recxy[0])
    # 调用图片处理
    #filepath = "./report/image/shujia_1.png"
    image.pic_rectangle(filepath, recxy)

#提取坐标
def  get_bounds_xy(bouds):
    #[488,308][668,368]
    xx,yy=bouds.split('][')
    print(xx,yy)
    x1,y1=xx.split(",")
    x1=x1.split('[')[1]
    x2,y2=yy.split(",")
    y2 = y2.split(']')[0]
    print('提取坐标x1, y1, x2, y2---------------', int(x1), int(y1), int(x2), int(y2))
    return int(x1), int(y1), int(x2), int(y2)



# 调用
filepath = "./report/image/shujia_2.jpg"
bound = [[488,308],[668,368]]
image.pic_rectangle2(filepath, bound)


#获取坐标
recxy=get_bounds_xy(t)
print(recxy,recxy[0])
#调用图片处理
filepath = "./report/image/shujia_1.png"
image.pic_rectangle(filepath, recxy)





