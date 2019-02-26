#coding:utf-8
from appium import webdriver
import time,os

import getxml  as xmlfile
import common
from appium.webdriver.common.touch_action import TouchAction 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))



"""
实现功能，单页面操作，id，name,class,
getsource_clicks    
click_elements_onenew
count_element
is_new_activity
1.搜索页，返回2次
2.点击操作，判断是否是跳转新页，是则返回
3.返回时，判断是否有弹窗，弹框点击确定
4.重复元素，点击操作
5.点击我的，back
6.点击书架，判断是否有弹窗

"""

#py3.4
#import app_kuaikan_new
#from imp import reload
#reload(app_kuaikan_new)

#统计文件
num=1
#进入主界面，判断弹窗
huodong="com.ishugui:id/imageview_close"

#设备及安装包信息
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
driver.implicitly_wait(10)


#获取屏幕宽度和高度
def getSize():
	global driver
	x = driver.get_window_size()['width']
	y = driver.get_window_size()['height']
	return (x, y)

#向左滑动
def swipeLeft():
	global driver
	s= getSize()
	x1 = int(s[0] * 0.9)
	y1 = int(s[1] * 0.5)
	x2 = int(s[0] * 0.1)
	driver.swipe(x1, y1, x2, y1)

#弹窗点击关闭，id=com.ishugui:id/imageview_cloud_sysch_close,
def  tanchuang(id):
	global driver
	try:
	        el=driver.find_element_by_id(id)
	        el.click()
	        print('关闭了弹窗')
	        
	except:
	        print('没有弹窗')

#取source
def get_pagesource():
        global driver
        r=driver.page_source
        if r:
                pass
                print("不空")
                print('pagesource:',r[:10])
                        
        else:
                print("空-----------------------------------------------")
        return r


print('----------------------------------------')
#id,name,class,操作
def click_all(name,act):
	global driver
	try:	
		if act=='id':
			el=driver.find_element_by_id(name)
		if act=='text':
			el=driver.find_element_by_name(name)
		if act=="class":
			el=driver.find_element_by_class_name(name)

		el.click()
		print('操作了',name)
	        
	except:
	        print('元素没有找到,',name)

# 获取当前界面activity
def get_current_activity():
	global driver
	ac = driver.current_activity
	#print('当前的activity:----------------',ac)
	return ac

'''
#------------------------------------------
#执行name长度大于20的字串，进行操作
def  click_elements(names,act,number=20):
	global num
	global level

	#当前操作
	cur_act={}
	#返回的操作存放
	cur_acts=[]
	#print(t)
    #统计操作次数	n
	n=0
	ac = get_current_activity(driver)
	for i in range(len(names)):
		print('正在执行%s,第%d-------------------------'%(act,i))
		#print(names[i])
		#执行text操作               
		t=names[i][3]['text']
		ids=names[i][3]['resource-id']
		classname=names[i][3]['class']
		#按text进行操作
		if act=='text':
			#text长度<=字符数，进行点击
			if len(t)<=number:	
				print('执行name--',t)	
				clickname(t)
				cur_act['text']=t
				n=n+1	
				#print(n)

		#点击id
		if act=='id':

				print('执行id--',ids,names[i][3]['text'])
				clickid(ids)
				cur_act['id']=ids
				n=n+1	
				#print(n)

		#点击class
		if act=="class":
				print('执行class--',classname,names[i][3]['text'])	
				clickclass(classname)
				cur_act['class']=clickname
				n=n+1	
				#print(n)

		#取activity，判断是否跳转到其他页面，如果是，返回
		new = get_current_activity()
		if ac!=new:
			print("跳转到其他页面了",new)
			#如果返回，就存放一下当前操作
			#get_pagesource()
			#如果跳转到其他页面，返回
			driver.back()
	print(n)
	return n,cur_acts


#将source存到文件，并取元素，--未调试完
def source_clicks(r,filenmae):
	#如果source 不为空
	if len(r)>10:
			#先将source写入xml文件中
			common.write_xml_to_file(filename,r)
			#从xml中取text，resource-id,属性元素
			names,ids,others=common.getAttrib_of_all(filename)
			if len(names)>0:
				#点击name
				print('names----------------个数',len(names))
				#点击name
				result=click_elements(names,'text')
				#调用执行
				re=back_clicks(result[0],len(names),result)

			if len(ids)>0:
				#点击id
				print('ids------------------个数',len(ids))
				result=click_elements(ids,'id')
				count=len(ids)
				#调用执行
				re=back_clicks(result[0],len(ids),result)

			if len(others)>0:
				#点击classname,
				#print('other-----------------个数',len(others))
				#result=click_elements(others,'class')

				#调用执行
				re=back_clicks(result[0],len(others),result)			
			return re


#-------------------------------
#执行results操作，有返回操作时存储
results=[]
def back_clicks(num,count,result): 
			global results   

			#有返回值
			if num!=count:
				for i in range(len(result)):
					results.append(result[i])
				return results
			#都执行完，没有返回时
			else:
				return False	

#------------------------------------------
#如果当前页面，变了，点击返回
def activity_now(cur,new):
	global driver
	if cur!=new:
		print("跳转到其他页面了",new,'正在返回')
		driver.back()
		return True
	else:
		return  False
#不用
#返回操作时，批判是否有书架弹窗，有则关闭，判断页面是否变了，变了，点击返回
def goback_clicks():
	#返回时判断书架是否有弹窗，有则关闭
	tanchuang(huodong)
	#有弹窗，点击确定，取消
	clickname("确定")
'''	
#------深度

'''
#当前页面source,只操作当前页面，有跳转，返回
def source_clicks_one(r,filename):
	ac = get_current_activity()	
	#如果source 不为空
	if len(r)>10:
			n=0
			#先将source写入xml文件中
			common.write_xml_to_file(filename,r)
			#从xml中取text，resource-id,属性元素
			names,ids,others=common.getAttrib_of_all(filename)

			#点击name
			print('names----------------个数',len(names))
			click_elements_one(names,'text')
			#点击id
			print('ids------------------个数',len(ids))
			click_elements_one(ids,'id')	        
			#点击classname,
			#print('other-----------------个数',len(others))
			#click_elements_one(others,'class')
			#print('操作了id %d次')

	return len(names),len(ids),len(others)

'''

#执行name长度大于20的字串，进行操作
def  click_elements_oneold(names,act,number=20):
	global driver
	#当前操作
	cur_act={}
	#返回的操作存放
	cur_acts=[]
	#print(t)
    #统计操作次数	n
	n=0
	ac = get_current_activity()
	for i in range(len(names)):
		print('正在执行%s,第%d-------------------------'%(act,i+1))
		#print(names[i])
		#只返回一个值时用
		t=names[i]
		ids=t
		classname=t
		#按text进行操作
		if act=='text':
			#text长度<=字符数，进行点击
			if len(t)<=number:
				print('执行%s---'%act,t)
				click_all(t,act)
				cur_act['text']=t				
				n=n+1	
		else:
				print('执行%s---'%act,t)
				click_all(t,act)
				cur_act['text']=t				
				n=n+1	

		#取activity，判断是否跳转到其他页面，如果是，返回
		new = get_current_activity()
		is_new_activity(ac,new)

	return n

#执行name长度大于20的字串，进行操作
#重复元素，操作
def  click_elements_onenew(names,act,number=20):
	global driver
	#当前操作
	cur_act={}
	#返回的操作存放
	cur_acts=[]
	#print(t)

	#-------------------------------
	#存放names
	temp_names=names
	#存放重复值
	repeat_element=[]
	flag=False
	print('去重复前--------------',len(names),names)
	for i in range(len(names)):
		#取当前元素		
		t=names[i]
		print('当前----------------',i,t)

		#已经有了的，不在存了
		if t in repeat_element:
			continue
		#判断有重复的进行，存放到数组中，并进行操作
		flag=count_element(names,t,act)	
		#print('----------------------------重复返回值',flag)	
		if flag:
			repeat_element.append(t)
			#如果存在多一个一样的元素，调用批量操作
			flag=False
	
	#有重复,进行删除
	print('重复----------------------',repeat_element)
	if len(repeat_element)>0:
		for x in repeat_element:
			for i in range(len(names)):
				if x in names:
					temp_names.remove(x)
			print('已去除重复',x)
	
	#names删除后
	names=temp_names
	print('去重复后--------------',len(names),names)	

	#执行其他操作
	#统计次数
	n=0
	ac = get_current_activity()
	for i in range(len(names)):
		print('正在执行%s,第%d-------------------------'%(act,i+1))
		#print(names[i])
		#只返回一个值时用
		t=names[i]
		#按text进行操作
		if act=='text':
			#text长度<=字符数，进行点击
			if len(t)<=number:
				print('执行%s---'%act,t)
				click_all(t,act)

				if t=="书架":
					#关闭弹窗，点击返回
					tanchuang(huodong)
				elif t in ["书架","分类","书城","我的"]:
					now=get_current_activity()
					if "Main2Activity" in now:
						driver.back()
						print('点击菜单操作---------------------')

				cur_act['text']=t				
				n=n+1	

		else:
				print('执行%s---'%act,t)
				click_all(t,act)
				cur_act['text']=t				
				n=n+1	

		#取activity，判断是否跳转到其他页面，如果是，返回
		new = get_current_activity()
		is_new_activity(ac,new)
	return n

#判断操作
def   click_menu(t):
		global driver
		if t=="书架":
			#关闭弹窗，点击返回
			tanchuang(huodong)
		elif t in ["书架","分类","书城","我的"]:
			now=get_current_activity()
			if "Main2Activity" in now:
				driver.back()
				print('点击菜单操作---------------------')

#判断是否新页面，是则返回
def is_new_activity(ac,new):
		global driver		
		if ac!=new:
			print("跳转到其他页面了",new,'正在返回-----')
			#如果跳转到其他页面，返回
			driver.back()
			new=get_current_activity()
			#返回时判断书架是否有弹窗，有则关闭
			tanchuang(huodong)
			if  "ReaderActivity" in  new:
				#有弹窗，点击确定，取消
				clickname("确定")
			#跳转到搜索，返回2次
			if "SearchActivity" in new:
				driver.back()
			print("已返回")


#取一样的元素,click,有重复，有则返回元素组
def count_element(names,e,act):
	global driver
	ac=get_current_activity()
	count=names.count(e)
	#当有多个一样的值是，执行find_elements
	el_counts=[]
	if count>1:

		if act=='id':
			el_counts=driver.find_elements_by_id(e)
		elif act=="text":
			el_counts=driver.find_elements_by_name(e)
		elif act=='class':
			el_counts=driver.find_elements_by_class(e)
		print('存在多个----------------------------',e)
		#操作
		for i in range(len(el_counts)):
			el_counts[i].click()
			print('正在点击多个%s,第%d个--------'%(act,i+1),e)
			#判断页面是否跳转
			new=get_current_activity()
			is_new_activity(ac,new)

		return True
	else:
		return 	False

#获取当前页面的pagesource，并执行操作
def  getsource_clicks(name):
	global num
	global driver

	num=num+1
	#获取当前页面pagesource
	r=get_pagesource()
	#ac = get_current_activity(driver)
	#存储文件名
	filename="%s_page_%s.xml"%(name,num)

	#调用函数--------------------------------------
	#re=source_clicks_one(r,filename)
	ac = get_current_activity()	
	#如果source 不为空
	if len(r)>10:
			n=0
			#先将source写入xml文件中
			common.write_xml_to_file(filename,r)
			#从xml中取text，resource-id,属性元素
			names,ids,others=common.getAttrib_of_all(filename)

			#点击name
			print('names----------------个数',len(names))
			click_elements_onenew(names,'text')
			#点击id
			print('ids------------------个数',len(ids))
			#click_elements_oneold(ids,'id')	        
			#点击classname,
			#print('other-----------------个数',len(others))
			#click_elements_one(others,'class')
			#print('操作了id %d次')

	return len(names),len(ids),len(others)
