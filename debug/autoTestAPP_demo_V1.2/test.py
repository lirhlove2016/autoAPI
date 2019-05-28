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


y1=1000
y2=1100
y3=1200
print("点击操作")
app.tap_point(0.2,y1)
time.sleep(2)
app.tap_point(0.5,y2)
time.sleep(2)
app.tap_point(0.9,y3)
time.sleep(2)
app.tap_point(0.9,y1)
time.sleep(2)
app.tap_point(0.5,y2)
time.sleep(2)
app.tap_point(0.2,y3)






