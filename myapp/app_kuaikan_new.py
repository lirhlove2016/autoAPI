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

'''
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
'''

#书架-今日签到
e=driver.find_element_by_id("com.ishugui:id/tv_sign_status")

time.sleep(5)
#text
text=e.text
print(text)
time.sleep(5)

print('-------------------')
#name="text"

attributes=["resourceId","className","text","name","checkable","checked","clickable","enabled","focusable","focused","scrollable","selected"]
alls=["text","tag_name","size","loaction"]

#定位元素e获取属性
def get_value(name,e):
	global alls,attributes,driver
	print('正在取值----------------------------------',name,e)
	if name in attributes:
		t=e.get_attribute(name)
		print(t)

	elif name in alls:
		if name=="text":
			t=e.text
		elif name=="tag_name":
			t=e.tag_name
		elif name=="size":
			t=e.size
		elif name=="loaction":
			t=e.location
		print(t)
	else:
		print("输入未找到：",name)
		t="fail"
	return t

#assert,name校验结果，value取值,e定位元素
def assert_equal(name,value,e):
	print('正在进行校验-----------------------------------------------------------------')
	print('本次校验的期望结果是：%s,取值%s'%(name,value))
	#调用取值
	values=get_value(value,e)
	#进行判断
	if name==values:
		print('校验正确,校验结果：%s'%name)

	else:
		print('校验不正确，要校验的值为%s,取值%s'%(value,values))

assert_equal("今日签到","text",e)
#批量定位






'''
#获取当前activity
s=driver.current_activity()
print(S)
'''
'''
#关闭应用，其实就是按home键把应用置于后台
s=driver.close_app()
print('close',s)
#启动应用
s=driver.launch_app()
print('alunch',s)


#点击(x,y)点按下，duration*5毫秒后松开，如此重复fingers次
s=driver.tap([(100,100),(100,200)],100)
print('tap',s)

'''



'''
#将某一个APP置于后台，3s钟后再调回前台
driver.background_app(3)
print('已经重新调回前台...')


driver.quit()
print('已经退出...')
'''


