#coding:utf-8
from appium import webdriver
import time,os

import pickle
import getxml  as xmlfile


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
#点击操作
#点击(x,y)点按下，duration*5毫秒后松开，如此重复fingers次
s=driver.tap([(48,261),(1032,476)],100)
print('tap点击操作了',s)

#检查应用是否已经安装 参数包名
driver.is_app_installed('com.ishugui')
adb="adb shell input keyevent 3"
os.system(adb)
'''

def get_pagesource():
	r=driver.page_source
	if r:
		pass
		print("不空")
		#print(r)
	else:
		print("空-----------------------------------------------")
	
#get_pagesource()

def clickid(name):
	try:
	        el=driver.find_element_by_id(name)
	        el.click()
	        print('操作了',name)
	        driver.get_pagesource
	        
	except:
	        print('元素没有找打')




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

#分类
fenlei_id="com.ishugui:id/textView"
click_fenlei=clickid(fenlei_id)   
print("点击了分类-------------------------------------")
driver.find_element_by_name("分类").click()
get_pagesource()

#2级
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
#3级
book_id="com.ishugui:id/imageview"
print("点击了3级分类-------------------------------------")
driver.find_element_by_name("桃运小村医").click()
'''
print(type(s))
#xml 存到文件中
#with open(r"d:\fenlei_write.xml","w+") as f:
with open(r"d:\\fenlei_write.xml","w") as f:
	#s1=s.encode()
	f.write(s)
	print("写入xml到文件")

#调用 xml
file_name = 'd:\\444.xml'
R = xmlfile.getXmlNode(file_name)

def clickname(name):
	try:
	        el=driver.find_element_by_name(name)
	        el.click()
	        print('操作了',name)
	        
	except:
	        print('元素没有找到,',name)


t=[]
p=[]
#提取不同分类
for x in R: 
	#print(x)
	if x[2]=="android.widget.TextView":
		t.append(x)

	elif x[2]=="android.widget.ImageView":
		p.append(x)

# 获取当前界面activity
ac = driver.current_activity
print('当前的activity----------------',ac)

#对分类进行操作
print('----------------------------')
def  go_el(t):
	n=0
	#print(t)
	for i in range(len(t)):
			#print(t[i])
			name=t[i][3]["text"]
			if len(name)<=10:
				clickname(name)
				n=n+1	
			#取activity
			new = driver.current_activity
			if ac!=new:
				print("跳转到其他页面了")
				print(new)
				get_pagesource
	print(n)
#-------------------------------
#取同一个属性的值
def  getAttrib(filename,name):
    R= xmlfile.getXmlNode(file_name)
    t=[]
    #提取不同分类
    for x in R: 
        #print(x)
        if x[2]==name:
            t.append(x)
    return t
    

 #---------------------------------



go_el(t)

def  go_eld(t):
	n=0
	for i in range(len(t)):
			#print(t[i])
			id=t[i][3]["resource-id"]
			driver.find_element_by_id(id)
			#取activity
			new = driver.current_activity
			if ac!=new:
				print("跳转到其他页面了")
				print(new)
			n=n+1	
	print(n)

go_eld(p)

#
s=driver.find_element_by_name("乡村").click()
print('s------',s)

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


#返回
'''
#打开通知栏（打开下拉通知栏）
s=driver.open_notifications()
print("下拉通知栏")
time.sleep(2)
print(s)
#点击爱转客
s=driver.tap([(580,101),(748,269)],100)
#获取当前Activity
s=driver.current_activity
print(s)
'''

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
'''
#书架-今日签到
e=driver.find_element_by_id("com.ishugui:id/tv_sign_status")

time.sleep(5)
#text
text=e.text
print(text)
time.sleep(5)

'''





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


