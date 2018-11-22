# coding:utf-8
from common import elementApp as app
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
import re
import time

#app.update_capability("appPackage","diankan")
print(app.desired_caps)

url="http://localhost:4723/wd/hub"
timeout=5
print('正在启动...')
app.start(url,timeout)

print('启动客户端.....')

time.sleep(5)

print('打开客户端了')

#启动页向左滑动
app.swip("left","3")



#点击男
app.get_element("id","com.ishugui:id/tv_man","","man")
app.click("click","man",)
print('已经滑动到第3页，正在选择男 女 ...')

'''
driver=app.driver
el=driver.find_element_by_id("com.ishugui:id/tv_man")
result=el.click()

print('定位元素-----------------',el,result)
print('点击结果-----------------',result)
'''
