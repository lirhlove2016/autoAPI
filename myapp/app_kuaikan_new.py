#coding:utf-8
from appium import webdriver
import time,os

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
#py3.4
#import app_kuaikan_new
#from imp import reload
#reload(app_kuaikan_new)


#获取屏幕宽度和高度
def getSize():
	x = driver.get_window_size()['width']
	y = driver.get_window_size()['height']
	return (x, y)

#向左滑动
def swipeLeft():
	s= getSize()
	x1 = int(s[0] * 0.9)
	y1 = int(s[1] * 0.5)
	x2 = int(s[0] * 0.1)
	driver.swipe(x1, y1, x2, y1)

#设备及安装包信息
# 'resetKeyboard': 'True'   #运行完成后重置软键盘的状态   #此两行是为了解决字符输入不正确的问题
# 'unicodeKeyboard': 'True',  #更改测试机的输入法

desired_caps = {
    'platformName': 'Android',
    'deviceName':'T8B6W4LJU4VSQWWW', #6EB0217518004226  
    'platformVersion': '6.0',
    #'app': PATH(r'E:\download\389.apk'), #安装目录
    'appPackage': 'com.ishugui',  
    'appActivity': 'com.dzbook.activity.LogoActivity',
    # 'resetKeyboard': 'True'   
    # 'unicodeKeyboard': 'True',  
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)

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

#男，resource=id=com.ishugui:id/tv_man ，text=男生小说
#女，com.ishugui:id/tv_woman，女生小说
driver.find_element_by_id("com.ishugui:id/tv_man").click()

#driver.find_element_by_id("com.ishugui:id/tv_woman").click()
#driver.find_element_by_id("com.ishugui:id/btn_guide_jump").click()
print('您选择了 “男生小说”')

#进入主界面
#弹窗点击关闭，id=com.ishugui:id/imageview_cloud_sysch_close,
try:
        el=driver.find_element_by_id("com.ishugui:id/imageview_cloud_sysch_close")
        el.click()
        print('关闭了弹窗')
        
except:
        print('没有弹窗')

print('点击我的')
#定位到我-文字-10环境
e2=driver.find_element_by_xpath("//android.widget.TextView[@text='我的']")
time.sleep(5)
print(e2)
e2.click()
time.sleep(2)
print('定位到我文字')
#定位图标
xpath="//android.widget.LinearLayout[@resource-id='com.ishugui:id/layout_navigationContainer']/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
e3=driver.find_element_by_xpath(xpath)
e3.click()
time.sleep(5)
print(e3)
print('定位到我的图标')

print('点击书架')
driver.find_element_by_id("com.ishugui:id/imageView").click()
time.sleep(5)

print('当前正在书架...')

xpath=".//*"
e=driver.find_element_by_xpath(xpath)
print("xpath",e)
time.sleep(5)

e=driver.current_context
print("context",e)
time.sleep(5)



#书架-今日签到
e=driver.find_element_by_id("com.ishugui:id/tv_sign_status")

time.sleep(5)
#text
text=e.text
print(text)
time.sleep(5)
#tag_name=calss
tag_name=e.tag_name
print(tag_name)
time.sleep(5)

#get attribute,get_attribute("contentDescription")
#如果content-desc为空，获取的text，不为空显示此内容
desc=e.get_attribute("contentDescription")
print(desc)
time.sleep(5)

#name,checkable,text,id,class,enabled,clickable,scrollable,password,selected
"resourceId","className","text"

attributes=["checkable","checked","clickable","enabled","focusable","focused","scrollable","selected"]
name="checkable"
name=e.get_attribute("checkable")


#size,location
s=e.size
l=e.loaction
print("size",s,"location",l)


#书架-搜索
driver.find_element_by_id("com.ishugui:id/iv_top_title_search").click()
time.sleep(5)
print("搜索")


'''
#将某一个APP置于后台，3s钟后再调回前台
driver.background_app(3)
print('已经重新调回前台...')


driver.quit()
print('已经退出...')
'''


