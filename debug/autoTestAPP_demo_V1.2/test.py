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


#我的-充值
xpath="//android.widget.TextView[@text='我的']"
el=driver.find_element_by_xpath(xpath).click()
print("打开我的")
#点击充值
xpath="com.ishugui:id/textview_click"
el=driver.find_element_by_id(xpath).click()
print("充值中心")
time.sleep(2)


#微信充值

#up 上滑
app.swiptest("up", "2")
print("上滑")
#微信支付
xpath="//android.widget.TextView[@text='微信']"
el=driver.find_element_by_xpath(xpath).click()
print("微信")

#down 下滑
app.swiptest("down", "1")
print("下滑")
xpath="//android.widget.TextView[@text='1看点']"
el=driver.find_element_by_xpath(xpath).click()
print("1看点")

#点击立即充值
xpath="//android.widget.TextView[@text='立即充值']"
el=driver.find_element_by_xpath(xpath).click()
print("点击充值")
time.sleep(1)
xpath="//android.widget.TextView[@text='立即支付']"
xpath="//*[contains(@text, '立即支付')]"
el=driver.find_element_by_xpath(xpath).click()
time.sleep(1)
print("点击支付")

'''
#支付宝--------------------------------
#up 上滑
app.swiptest("up", "2")
print("上滑")
#支付
xpath="//android.widget.TextView[@text='支付宝']"
el=driver.find_element_by_xpath(xpath).click()
print("支付宝")

#down 下滑
app.swiptest("down", "1")
print("下滑")
xpath="//android.widget.TextView[@text='100看点']"
el=driver.find_element_by_xpath(xpath).click()
print("100看点")

#点击立即充值
id="com.ishugui:id/textview_recharge"
xpath="//android.widget.TextView[@text='立即充值']"
el=driver.find_element_by_xpath(xpath).click()

time.sleep(1)
xpath="//android.widget.TextView[@text='立即付款']"
el=driver.find_element_by_xpath(xpath).click()
time.sleep(1)
#支付宝充值
key=1
xpath="//android.widget.TextView[@resource-id='com.alipay.android.phone.safepaybase:id/key_num_%s']"%key
el=driver.find_element_by_xpath(xpath).click()

key=5
xpath="//android.widget.TextView[@resource-id='com.alipay.android.phone.safepaybase:id/key_num_%s']"%key
el=driver.find_element_by_xpath(xpath).click()
key=9
xpath="//android.widget.TextView[@resource-id='com.alipay.android.phone.safepaybase:id/key_num_%s']"%key
el=driver.find_element_by_xpath(xpath).click()
key=3
xpath="//android.widget.TextView[@resource-id='com.alipay.android.phone.safepaybase:id/key_num_%s']"%key
el=driver.find_element_by_xpath(xpath).click()
key=5
xpath="//android.widget.TextView[@resource-id='com.alipay.android.phone.safepaybase:id/key_num_%s']"%key
el=driver.find_element_by_xpath(xpath).click()
key=7
xpath="//android.widget.TextView[@resource-id='com.alipay.android.phone.safepaybase:id/key_num_%s']"%key
el=driver.find_element_by_xpath(xpath).click()
'''

time.sleep(5)
print('开始操作按键')

#按键1 8，KEYCODE_1
s=driver.press_keycode(8)   #括号里填入的是键盘按键的数字代号
time.sleep(2)
print('按键1',s)
s=driver.press_keycode(12)   #括号里填入的是键盘按键的数字代号
print('按键3',s)

s=driver.press_keycode(16)   #括号里填入的是键盘按键的数字代号

#微信密码输入键盘，三等分
def split_xy(x1, x2):
    x11 = int((x2 - x1) / 3)
    x12 = int((x2 - x1) / 3 * 2)
    x13 = int((x2 - x1) / 3 * 3)

    return x11, x12, x13

#[1,929][719,1036]
#[1,1036][719,1143]
#[1,1143][719,1251]
x1=1
x2=929
y1=1000

x11=int((x2-x1)/3)
x13=x2
print("点击键盘159，357")
x11,x12,x13=split_xy(1,929)
app.tap_point(x11,y1)

y2=1000
x21,x22,x23=split_xy(1,1036)
app.tap_point(x22,y2)

y3=1200
x31,x32,x33=split_xy(1,1143)
app.tap_point(x13,y3)
print("点击键盘357")
#3
app.tap_point(x13,y1)
#5
app.tap_point(x22,y2)
#7
app.tap_point(x31,y3)





