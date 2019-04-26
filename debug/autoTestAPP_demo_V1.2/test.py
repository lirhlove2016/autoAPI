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
app.update_capability('platformVersion','9')
app.update_capability('deviceName','UYT0218209004285')
app.update_capability('appPackage','com.ishugui')
app.update_capability('appActivity','com.dzbook.activity.LogoActivity')
app.update_capability('automationName','UiAutomator2')

#引用你要调试的文件中的driver
#app.start('http://localhost:4723/wd/hub',30)

# 保存图片
resultfile = os.path.join(reportDir, 'image/pic')
num=1

driver=app.driver
time.sleep(5)
#截图
app.get_screenshot(resultfile, "_1.png")
print('保存图片了')

filepath=resultfile+"_1.png"

#取bounds
el=app.get_element("text","今日签到","","shujia")
el=driver.find_element_by_id("com.ishugui:id/tv_sign_status")
print(el)
t=el.get_attribute("bounds")
print("获取的bounds",t,type(t))

#拆分
def get_bounds(t):
    print('正在拆分')
    x=t.split('][')
    x1,y1=x[0].split(',')
    x2,y2=x[1].split(',')
    p1=x1.split('[')
    p2=y2.split(']')
    x1=p1[1]
    y2=p2[0]
    return  int(x1),int(x2),int(y1),int(y2)
x=get_bounds(t)
print('x',x)
b=[]
c=[]
d=[]
b.append(x[0])
b.append(x[1])
c.append(x[2])
c.append(x[3])
d.append(b)
d.append(c)
print('d',d)

# 调用
filepath=resultfile+"_2.png"
#d=[[488, 668], [308, 368]]
print(filepath,d)
image.pic_rectangle(filepath, d)


#点击
#el.click()

