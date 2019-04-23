#coding:utf-8
from appium import webdriver
import time,os

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


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
#deviceNam #指定需要控制的设备，在控制台中输入adb devices 就会出现deviceName
#被测试程序的packageName，在控制台中输入adb logcat | grep(findstr) START
# 'resetKeyboard': 'True'   #运行完成后重置软键盘的状态   #此两行是为了解决字符输入不正确的问题
# 'unicodeKeyboard': 'True',  #更改测试机的输入法

desired_caps = {
    'platformName': 'Android',
    'deviceName':'T8B6W4LJU4VSQWWW', #6EB0217518004226  
    'platformVersion': '6.0',
    #'app': PATH(r'E:\download\385.apk'), #安装目录
    'appPackage': 'com.ishugui',  
    'appActivity': 'com.dzbook.activity.LogoActivity',
    # 'resetKeyboard': 'True'   
    # 'unicodeKeyboard': 'True',  
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)


#启动activity
#driver.start_activity('com.ishugui','.com.dzbook.activity.LogoActivity')#参数：1包名，参数2：activity名


print('正在启动客户端.....')
time.sleep(5)
print('打开客户端了')


print('启动页滑动...')
'''
#启动页向左滑动
i=0
while i <3:
    swipeLeft()
    i=i+1
'''
#swip =driver.find_element_by_class("android.widget.ImageView")
#swip.click()

print('已经滑动到第3页，正在选择男 女 ...')

#男，resource=id=com.ishugui:id/tv_man ，text=男生小说
#女，com.ishugui:id/tv_woman，女生小说
#跳过，com.ishugui:id/btn_guide_jump，跳过
#新用户更有好礼相赠，class=android.widget.TextView,text=新用户更有好礼相赠
#driver.find_element_by_id("com.ishugui:id/tv_man").click()
el=driver.find_element_by_id("com.ishugui:id/tv_man")
result=el.click()
print('定位元素-----------------',el,result)
print('点击结果-----------------',result)
#driver.find_element_by_id("com.ishugui:id/tv_woman").click()
#driver.find_element_by_id("com.ishugui:id/btn_guide_jump").click()
print('您选择了 “男生小说”')
'''
#进入主界面
#弹窗点击关闭，id=com.ishugui:id/imageview_cloud_sysch_close,
try:
        el=driver.find_element_by_id("com.ishugui:id/imageview_cloud_sysch_close")
        el.click()
        print('关闭了弹窗')
        
except:
        print('没有弹窗')
'''

#点击我的
#我的图片，id=com.ishugui:id/imageView,
#我的文字，id=com.ishugui:id/textView,text=我的

print('点击我的')
driver.find_elements_by_android_uiautomator("new UiSelector().text(\"我的\")")
time.sleep(5)

print('点击书架')
driver.find_element_by_id("com.ishugui:id/imageView").click()
time.sleep(5)

print('当前正在书架...')

#将某一个APP置于后台，3s钟后再调回前台
driver.background_app(3)
print('已经重新调回前台...')


driver.quit()


