# coding:utf-8
from common import elementApp as app
from common import readexcel as reader, writeexcel as writer

from appium.webdriver.common.touch_action import TouchAction
import time
import os
import random


# -文件目录配置----------------------------
filepath = os.path.abspath(os.getcwd())
srcfile = os.path.join(filepath, 'datadir/myApp.xls')
desfile = os.path.join(filepath, 'datadir/myApp_result123.xls')
resultfile = os.path.join(filepath, 'report/screenshot/screenshot_')
print(srcfile)

reader.open_excel(srcfile)
writer.copy_open(srcfile, desfile)

'''
app.update_capability("deviceName","T8B6W4LJU4VSQWWW")
app.update_capability("platformVersion","8.0")
app.desired_caps['unicodeKeyboard']=True
app.desired_caps['resetKeyboard']=True


print(app.desired_caps['unicodeKeyboard'])
print(app.desired_caps['resetKeyboard'])

'''
url="http://localhost:4723/wd/hub"
timeout=10
print('正在启动...')
app.start(url,timeout)
print('启动客户端.....')
app.sleep(1)
print('打开客户端了')


#启动页向左滑动
app.LEFT()
app.LEFT()
app.LEFT()

driver=app.driver

ret = driver.find_element_by_xpath("//*")
print('xpath--------',ret)
#点击男
print('已经滑动到第3页，正在选择男 女 ...')
app.get_element("id","com.ishugui:id/tv_man","","man",'selectman')
app.clicks("click","man")
print('选择男生，进入主界面')
app.sleep(1)
#close
'''
el=driver.find_element_by_id("com.ishugui:id/imageview_close")
el.click()
'''
app.sleep(2)



'''
print('正在搜素')
#搜素
el=driver.find_element_by_id("com.ishugui:id/iv_top_title_search")
el.click()

el=driver.find_element_by_id("com.ishugui:id/edit_search").send_keys("123")
el=driver.find_element_by_id("com.ishugui:id/edit_search")
el.send_keys("天天见")
time.sleep(5)

s1=driver.keyevent("4")
print('1---',s1)

'''

'''
s2=driver.keyevent(4)
print('2---',s2)
#driver.keyevent()        #括号里填入的是手机物理按键的数字代号

time.sleep(5)

s3=driver.press_keycode(4)   #括号里填入的是键盘按键的数字代号
time.sleep(2)
print('3---',s3)

s4=driver.press_keycode("4") 
print('4---',s4)

time.sleep(2)
l=driver.page_source

with  open('pagesource.xlm','w+') as f:
        f.write(l)
#print(l)
app.get_pages_source("shujia.xml")

re=app.get_page()
print('xpath--------',re)
ret = driver.find_element_by_xpath("//*")
print('xpath--------',ret)

print('end----------------')
'''
r=app.get_xy('0.5','0.5')

print(r)

x=r[0]
y=r[1]
print(x,y)

#随机点击一次
app.tap_random()
time.sleep(2)


#坐标点击
print("坐标点击:" + str(x),str(y))
app.tap_point('0.5','0.5')
time.sleep(2)
ac = app.get_current_activity()
print(ac)

if  "ReaderActivity"  not in   ac:
        print('没有进入阅读器')
        app.tap_point(x,y)        
        ac = app.get_current_activity()
else:
        print('进入阅读器')

#再次点击，如果是第一次进入，需要再次点击
#点击2次再次打开菜单

time.sleep(2)
reader=driver.page_source
#print(reader)

app.tap_point('0.5','0.5')
app.tap_point('0.5','0.5')

reader=driver.page_source
#print(reader)
app.source_assert("下一章")

#点击下一章
el=driver.find_element_by_name('下一章')
el.click()
time.sleep(2)

print('点击中间，菜单出来，点击下一章了')
app.tap_point('0.5','0.5')

time.sleep(2)
app.source_assert("上一章")
#上一章
el=driver.find_element_by_name('上一章')
el.click()
time.sleep(2)

print('点击中间，菜单出来，点击上一章了')
app.tap_point('0.5','0.5')


time.sleep(2)
app.source_assert("设置")
#设置
el=driver.find_element_by_name('阅读设置')
el.click()
print('点击中间，菜单出来，点击设置了')




