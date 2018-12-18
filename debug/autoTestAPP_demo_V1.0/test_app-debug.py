# coding:utf-8
from common import elementApp as app
from common import readexcel as reader,writeexcel as writer
from conf.conf import *

#-文件目录配置----------------------------
#conf配置
srcfile=os.path.join(dataDir,'myApp.xls')
desfile=os.path.join(dataDir,'myApp_result.xls')
resultfile=os.path.join(reportDir,'screenshot/screenshot_')
print(dataDir,srcfile)

#conf配置
srcfile=os.path.join(dataDir,'myApp.xls')
desfile=os.path.join(dataDir,'myApp_result.xls')
resultfile=os.path.join(reportDir,'screenshot/screenshot_')
print(dataDir,srcfile)


#app.update_capability("appPackage","diankan")
print(app.desired_caps)
app.update_capability("deviceName","6EB02175180042260")
#app.update_capability("platformVersion","8.0")
print(app.desired_caps)

url="http://localhost:4723/wd/hub"
timeout=10
print('正在启动...')
app.start(url,timeout)

print('启动客户端.....')

time.sleep(5)

print('打开客户端了')

#启动页向左滑动
app.swiptest("left","3",100)


#点击男
print('已经滑动到第3页，正在选择男 女 ...')
app.get_element("id","com.ishugui:id/tv_man","","man")
app.click("man",)
print('选择男生，进入主界面')


driver=app.driver
el=driver.find_element_by_id("com.ishugui:id/tv_man1")
result=el.click()

print('定位元素-----------------',el,result)
print('点击结果-----------------',result)





