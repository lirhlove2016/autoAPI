#coding:utf-8
from appium import webdriver
import time,os

import getxml  as xmlfile
import common
from appium.webdriver.common.touch_action import TouchAction 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    "chromeOptions":{"androidProcess":"WEBVIEW_com.android.quicksearchbox"},
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
def  tanchuang(name):
	try:
	        el=driver.find_element_by_id(name)
	        el.click()
	        print('关闭了弹窗')
	        
	except:
	        print('没有弹窗')


def get_pagesource():
	r=driver.page_source
	if r:
		pass
		print("不空")
		#print(r)
	else:
		print("空-----------------------------------------------")
	
def clickid(name):
	try:
	        el=driver.find_element_by_id(name)
	        el.click()
	        print('操作了',name)
	        driver.get_pagesource
	        
	except:
	        print('元素没有找到',name)



	        
time.sleep(2)
def clickname(name):
	try:
	        el=driver.find_element_by_name(name)
	        el.click()
	        print('操作了',name)
	        
	except:
	        print('元素没有找到,',name)
	        
print('----------------------------')
def  go_el(t):
	n=0
	#print(t)
	ac = driver.current_activity
	for i in range(len(t)):
			#print(t[i])
			#text长度<=字符进行点击
			name=t[i][3]["text"]
			if len(name)<=10:
				clickname(name)
				n=n+1	
				#取activity
				new = driver.current_activity

				if ac!=new:
					print("跳转到其他页面了")
					print(new)
					#get_pagesource
					driver.back()
	print(n)


#h5
print('all',driver.contexts)
c=driver.contexts
print('current',driver.current_context)


'''
try:
    WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//*[@text="登录"]')).click()
    print('立即登录')
except:
    print('登录弹窗未出现')

'''

#----------------------------------------------
text="text"
id="resource-id"
#获取到 pagesouce，就取值，text，id，然后点击操作
r=driver.page_source
if len(r)>1:
 
        filename="h5.xml"
        time.sleep(2)
        #
        common.write_xml_to_file(filename,r)
        t=common.getAttrib(filename,"android.widget.Button")
        print('pagesource,',r,t)

        go_el(t)
        print('current',driver.current_context)

#----------------------------------------------
driver.switch_to.context('WEBVIEW_com.android.quicksearchbox')

print('curr',driver.current_context)

try:
    text="立即使用"
    oc = ("xpath", ".//*[contains(@text,'%s')]"%text)
    print(loc)
    e=WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
    e.click()
except:
    pass


'''
try:
    log=""
    WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//*[@text="立即使用"]')).click()
    
    print('立即登录')
except:
    print('登录弹窗未出现')
'''


driver.switch_to.context('NATIVE_APP')
print('切换到app成功')


#e=driver.switch_to_alert() #切换到alert窗口

'''
tanchuang("com.ishugui:id/imageview_cloud_sysch_close")

#取x,y坐标的中间点，[331,968][499,1136]，左上，右下，x=400,y=1000
def do_tap(x,y):
	adb = 'adb shell input tap %s %s'%(x,y)
	os.system(adb)

#[331,968][499,1136]
#do_tap(400,1000)



#定位云菜单-云书架,[960,103][1065,208],
xpath="//android.support.v7.widget.RecyclerView[@resource-id='com.ishugui:id/rv_bookshelf']/android.widget.RelativeLayout[2]"
el=driver.find_element_by_xpath(xpath).click()
time.sleep(2)
print('点击了云菜单')
driver.tap([(960,103),(1065,208)],100)
el=clickid("com.ishugui:id/tv_shelf_menu_cloud")

print('点击了云书架单')
time.sleep(2)
#长按
s=TouchAction(driver).long_press().perform()
print("长按云书架",s)
#
driver.keyevent('4')  #4 返回 
driver.back()
tanchuang("com.ishugui:id/imageview_close")
#书架-今日签到
e=driver.find_element_by_name("今日签到")
driver.contexts
driver.current_context
driver.flick(100, 100, 100, 400)  #快速滑动
print('快速滑动')
print(driver.current_activity)
driver.background_app(3)   #置后台3秒后再运行
#e2=driver.find_element_by_name("本周已读")  #定位报错
driver.open_notifications()   #打系统通知栏（仅支持API 18 以上的安卓系统）
driver.back()
driver.drag_and_drop(e,e)
driver.scroll(e, e)
print('签到按钮滚动')
print(driver.network_connection)   #
print(driver.available_ime_engines)
print(driver.is_ime_active())  #检查设备是否有输入法服务活动。返回真/假。

#检查应用是否已经安装 参数包名
print(driver.is_app_installed('com.ishugui'))
driver.close_app()   #关闭app

'''
'''
#点击操作
#点击(x,y)点按下，duration*5毫秒后松开，如此重复fingers次
driver.tap([(48,261),(1032,476)],100)
print('tap点击操作了---',s)

def go_tap(driver,x,y,du):
	driver.tap([(48,261),(1032,476)],100)
#go_tap(driver,x,y,du)
'''

'''
#书架-搜索
sousuo_id="com.ishugui:id/iv_top_title_search"
click_sousou=click(sousuo_id)
#搜索-热词
word_id="com.ishugui:id/textview_content"
click_word=click(word_id)
driver.back()
get_pagesource()
time.sleep(2)
driver.back()
get_pagesource()
'''
'''
#分类
fenlei_id="com.ishugui:id/textView"
click_fenlei=clickid(fenlei_id)

print("点击了分类-------------------------------------")
driver.find_element_by_name("分类").click()
get_pagesource()

#2级com.ishugui:id/tv_shelf_menu_cloud
#都市
dushi_id="都市"
print("点击了2级分类-------------------------------------")
driver.find_element_by_name("都市").click()
time.sleep(2)
get_pagesource()
time.sleep(2)
get_pagesource()
s=driver.page_source
'''
'''
#3级
book_id="com.ishugui:id/imageview"
print("点击了3级分类-------------------------------------")
driver.find_element_by_name("桃运小村医").click()
'''
'''
filename="d:\\fenlei_write.xml"
common.write_xml_to_file(filename)



t=common.getAttrib(filename,"android.widget.TextView")



# 获取当前界面activity
def get_current_activity(driver):
	ac = driver.current_activity
	print('当前的activity----------------',ac)
	return ac
ac=get_current_activity(driver)


#对分类进行操作
print('----------------------------')
def  go_el(t):
	n=0
	#print(t)
	for i in range(len(t)):
			#print(t[i])
			#text长度<=字符进行点击
			name=t[i][3]["text"]
			if len(name)<=10:
				clickname(name)
				n=n+1	
				#取activity
				new = get_current_activity(driver)

				if ac!=new:
					print("跳转到其他页面了")
					print(new)
					get_pagesource
	print(n)

#go_el(t)
def  go_eld(t):
	n=0
	for i in range(len(t)):
			#print(t[i])
			x=t[i][3]["resource-id"]
			print(x,'------------------------------',len(x))
			if len(x)>1:
				driver.find_element_by_id(x)
				print('点击图片了')
				#取activity
				new = driver.current_activity
				if ac!=new:
					print("跳转到其他页面了")
					print(new)
				n=n+1	
	print(n)
print(p)
go_eld(p)


#
s=driver.find_element_by_name("乡村").click()
print('s------',s)


#---------------------------
'''
'''
#返回 取source
time.sleep(2)
driver.back()
get_pagesource()

time.sleep(2)
driver.back()
get_pagesource()

time.sleep(2)
driver.back()
get_pagesource()

time.sleep(2)
driver.back()
get_pagesource()
'''

'''

#返回

#打开通知栏（打开下拉通知栏）
s=driver.open_notifications()
print("下拉通知栏")
time.sleep(2)
print(s)


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
'''
#书架-今日签到
e=driver.find_element_by_id("com.ishugui:id/tv_sign_status")

time.sleep(5)
#text
text=e.text
print(text)
time.sleep(5)


#获取当前activity
s=driver.current_activity()
print(S)


#关闭应用，其实就是按home键把应用置于后台
s=driver.close_app()
print('close',s)
#启动应用
s=driver.launch_app()
print('alunch',s)

#将某一个APP置于后台，3s钟后再调回前台
driver.background_app(3)
print('已经重新调回前台...')


driver.quit()
print('已经退出...')
'''


