# coding:utf-8
from common import elementApp as app
from common import readexcel as reader, writeexcel as writer

from appium.webdriver.common.touch_action import TouchAction
import time
import os

# -文件目录配置----------------------------
filepath = os.path.abspath(os.getcwd())
srcfile = os.path.join(filepath, 'datadir/myApp.xls')
desfile = os.path.join(filepath, 'datadir/myApp_result123.xls')
resultfile = os.path.join(filepath, 'report/screenshot/screenshot_')
print(srcfile)


reader.open_excel(srcfile)
writer.copy_open(srcfile, desfile)


app.update_capability("deviceName","6EB0217518004226")
app.update_capability("platformVersion","8.0")
print(app.desired_caps)
app.update_capability("deviceName","6EB0217518004226")
app.update_capability("platformVersion","8.0")

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

#点击男
print('已经滑动到第3页，正在选择男 女 ...')
app.get_element("id","com.ishugui:id/tv_man","","man",'selectman')
app.clicks("click","man")
print('选择男生，进入主界面')
app.sleep(1)
#close
el=driver.find_element_by_id("com.ishugui:id/imageview_close")
el.click()

app.sleep(2)

print('正在搜素')
#搜素
el=driver.find_element_by_id("com.ishugui:id/iv_top_title_search")
el.click()

el=driver.find_element_by_id("com.ishugui:id/edit_search").send_keys("123")
el=driver.find_element_by_id("com.ishugui:id/edit_search")
el.send_keys("天天见")
time.sleep(5)
print('1---')
#driver.keyevent("4")
print('2---')
driver.keyevent(4)

#driver.keyevent()        #括号里填入的是手机物理按键的数字代号

time.sleep(5)
print('3---')
driver.press_keycode(4)   #括号里填入的是键盘按键的数字代号


'''
driver.sendKeyEvent(AndroidKeyCode.BACKSPACE);
driver.sendKeyEvent(AndroidKeyCode.DEL);
driver.sendKeyEvent(AndroidKeyCode.ENTER);
driver.sendKeyEvent(AndroidKeyCode.HOME);
driver.sendKeyEvent(AndroidKeyCode.MENU);
driver.sendKeyEvent(AndroidKeyCode.SETTINGS);
driver.sendKeyEvent(AndroidKeyCode.SPACE);
'''

print('定位元素-----------------')
print('点击结果-----------------')





