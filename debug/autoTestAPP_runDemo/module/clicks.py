#coding:utf-8
from appium import webdriver
import time,os
from appium.webdriver.common.touch_action import TouchAction 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import module.getxml  as xmlfile
from  module import common    as  common
from conf.conf import *

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
7.xml取元素，按配置
8.底部菜单不操作，按配置
9.弹窗配置,按配置执行，tanchuang_all
10.搜索页，点击后返回，1级，2级页面时，
11.输入框，随机取输入值
12.返回不操作，按配置
13.坐标点击
14.随机点击
15.上下左右滑动
16.xpath点击操作
17.保存图片，
18.框选点击位置


"""

#py3.4,重新加载模块
#import app_kuaikan_new
#from imp import reload
#reload(app_kuaikan_new)


#统计文件
num=0

#设备及安装包信息
desired_caps = {
    'platformName': 'Android',
    'deviceName':'T8B6W4LJU4VSQWWW', #6EB0217518004226  
    'platformVersion': '6.0',
    #'app': PATH(r'E:\download\389.apk'), #安装目录
    'appPackage': 'com.aikan',  
    'appActivity': 'com.dzbook.activity.LogoActivity',
    # 'resetKeyboard': 'True'   
    # 'unicodeKeyboard': 'True',
    "chromeOptions":{"androidProcess":"WEBVIEW_com.android.quicksearchbox"},
    'autoGrantPermissions': True,
    'newCommandTimeout':10,

}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#等待3s
driver.implicitly_wait(3)


#获取坐标bound
def get_bound(el):

	return el.get_attribute("bound")

def  image_shot():
    filename=imageDir + "nansheng.jpg"
    get_screenshot("nansheng.jpg")
    t=get_bound(el)
    print(t)
    pic_rectangle(filename,bound)

#-------------------------------------
# 保存图片到指定文件夹
def get_screenshot(file):
    global driver
    filename = imageDir + file
    print('正在保存图片', filename)
    try:
        driver.get_screenshot_as_file(filename)

    except Exception as err:
        #调用方法
        print('截图报错了')



#判断source中存在就点击
def xpath_menu(mechod,name):
	#根据text包含值，点击
	source=driver.page_source
	if name in source:
		x="//*[contains(@%s,%s)]"%(mechod,name)
		el=driver.find_element_by_xpath(x)	    	
		el.click()
		print('已经点击了',name)   

	else:
		print('不存在',name)
#-----------------------------------------------
# 获取尺寸
def getSize():
    global start_x, start_y, end_x, end_y
    start_x = 0
    start_y = 0
    end_x = driver.get_window_size()['width']
    end_y = driver.get_window_size()['height']
    return (start_x, start_y, end_x, end_y)
#-----------------------------------------------

#随机点击
def tap_random():
    R = []
    #生成2个随机数
    for i in range(2):
        r = random.randint(1, 10)/10
        R.append(r)
    #print(R)
    x = int(getSize()[2]*R[0])
    y = int(getSize()[3]*R[1])
    #print(str(x),str(y))
    try:
        print("即将随机点击：" + str(x),str(y))
        driver.tap([(x,y)])
        re="PASS"
        value="随机点击坐标%s,%s"%(str(x),str(y))       

    except BaseException as e:
        print("随机点击出错了%s"%str(e))
        re="FAIL"
        value="随机点击出错了%s"%str(e)

    # 写入
    #wirte_result(re,value)

#-----------------------------------------------        
#坐标点击
def tap_point(x,y):
    #如果输入坐标小于0，按比例提取坐标
    #如果传入是str类型，判断
    if type(x)==str:
        if x<'1':
            re=get_xy(x,y)
            x=re[0]
    elif x<1:
        re=get_xy(x,y)
        x=re[0]

    if type(y)==str:
        if y<'1':
            re=get_xy(x,y)
            y=re[1]
    elif x<1:
        re=get_xy(x,y)
        y=re[1]
 
        
    #print(str(x),str(y))
    print("即将点击坐标:" + str(x),str(y))
    try:
        driver.tap([(x,y)])
        re="PASS"
        value="点击坐标%s,%s"%(str(x),str(y))          

    except BaseException as e:
        
        print("点击出错了%s"%str(e))

        re="FAIL"
        value="点击出错了%s"%str(e)

    # 写入
    #wirte_result(re,value)

# 上划
def swipUp():
    try:
        x1 = int(getSize()[2] * 0.5)
        y1 = int(getSize()[3] * 0.2)
        y2 = int(getSize()[3] * 0.8)
        driver.swipe(x1, y2, x1, y1)

        value = "up"
        key = "PASS"
    except BaseException as err:
        print(err)
        value = str(err)
        key = "FAIL"

    # 写入
    wirte_result(key, value)


# 下划
def swipDown():
    try:
        x1 = int(getSize()[2] * 0.5)
        y1 = int(getSize()[3] * 0.2)
        y2 = int(getSize()[3] * 0.8)
        driver.swipe(x1, y1, x1, y2)

        value = "down"
        key = "PASS"
    except BaseException as err:
        print(err)
        value = str(err)
        key = "FAIL"

    # 写入
    #wirte_result(key, value)

# 左划
def swipLeft():
    try:
        x1 = int(getSize()[2] * 0.2)
        x2 = int(getSize()[2] * 0.8)
        y1 = int(getSize()[3] * 0.5)
        driver.swipe(x2, y1, x1, y1)

        value = "left"
        key = "PASS"
    except BaseException as err:
        print(err)
        value = str(err)
        key = "FAIL"

    # 写入
    #wirte_result(key, value)

# 右划
def swipRight():
    try:
        x1 = int(getSize()[2] * 0.2)
        x2 = int(getSize()[2] * 0.8)
        y1 = int(getSize()[3] * 0.5)
        driver.swipe(x1, y1, x2, y1)

        value = "right"
        key = "PASS"
    except BaseException as err:
        print(err)
        value = str(err)
        key = "FAIL"

    # 写入
    #wirte_result(key, value)

#----------------------------------------------
#弹窗点击关闭，id=com.ishugui:id/imageview_cloud_sysch_close,
def  tanchuang(id):
	global driver
	try:
	        el=driver.find_element_by_id(id)
	        el.click()
	        print('关闭了弹窗')
	        
	except Exception as  err:
	        print('弹窗报错了',err)


#----------------------------------------------
#弹窗关闭
def tanchuang_all():
	#从配置文件中取参数,id
	ids=tanchuang_close_id
	for x in ids:
		source=driver.page_source
		if x in source:
			print('正在关闭弹窗',x)
			tanchuang(x)
			
		else:
		    print('不存在弹窗id')

		
#----------------------------------------------
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
#---------------------------------------------
#程序运行时间
def run_time():
	return time.clock()

#----------------------------------------------
#输入框中随机输入值
def edit_input_value():
	value=random.choice(default_input_values)
	#value=random.sample(default_input_values, 1)
	return value

#----------------------------------------------
#id,name,class,操作
def click_all(name,act,method=""):
	global driver
	try:	
		if act=='id':
			el=driver.find_element_by_id(name)
		
		elif act=='text':
			el=driver.find_element_by_name(name)
		
		elif act=="class":
			el=driver.find_element_by_class_name(name)
		
		elif act=="xpath":
			el=driver.find_element_by_xpath(name)
	
		else:
			print('没有此方法--------',act,name)

		if method=="":
			el.click()
			print('点击了',name)
		elif method=="edit":
			#调用，获取输入值
			value=edit_input_value()
			el.send_keys(value)
			print('输入了',value)
		        
	except Exception as err:
	        print('元素没有找到,',act,name,err)


#findElements
def elements_all(name,act,method=""):
	global driver
	try:	
		if act=='id':
			el=driver.find_elements_by_id(name)
		elif act=='text':
			el=driver.find_elements_by_name(name)
		elif act=="class":
			el=driver.find_elements_by_class_name(name)
		elif act=="xpath":
			el=driver.find_elements_by_xpath(name)
		
		else:
			print("没有此方法,请检查",act)

		return el   
	
	except:
	        print('多个元素没有找到,',name)
	        return False

# 获取当前界面activity
def get_current_activity():
	global driver
	ac = driver.current_activity
	#print('当前的activity:----------------',ac)
	return ac


'''
#------------------------------------------
#执行name长度大于20的字串，进行操作,多层操作
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

#排除底部菜单
#排除返回
def exclude_menu(names):
	temp_names=names

	#print('菜单----------------------')
	for x in bottom_menu:
		for i in range(len(names)):
			if x in names:
				temp_names.remove(x)
				print('已去除菜单',x)
	
	#print('菜单----------------------')	
	for x in Notclick_name:
		#不执行的name
		for i in range(len(names)):
			if x in names:
				temp_names.remove(x)
				print('已去除不执行',x)
	#带返回的不执行
	for x in Notclick_back_include:
		#不执行的name
		for i in range(len(names)):
			if x in names:
				temp_names.remove(x)
				print('已去除不执行的back',x)	
	
	return  temp_names	
#执行name长度大于20的字串，进行操作
#重复元素，操作
def  click_elements_one_old(names,act,number=20):
	global driver
	#当前操作
	cur_act={}
	#返回的操作存放
	cur_acts=[]
	#print(t)
	#-------------------------------
	#1菜单 排除menu
	names=exclude_menu(names)

	#2调用重复，有重复进行操作
	names=repeat_elements_clicks(names,act)

	#执行其他操作
	#统计次数
	n=0
	ac = get_current_activity()
	for i in range(len(names)):
		print('正在执行%s,第%d-------------------------'%(act,i+1))
		#print(names[i])
		#只返回一个值时用


		#反着执行
		t=names[len(names)-i-1]

		#t=names[i]
		#按text进行操作
		if act=='text':
			#text长度<=字符数，进行点击
			if len(t)<=number:
				print('执行%s---'%act,t)			
				#输入框时，输入内容
				#method=""
				method=is_edit(t)
				#调用操作
				
				click_all(t,act,method)

				if t=="书架":
					#关闭弹窗，点击返回
					#tanchuang(huodong)
					tanchuang_all()
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

#传所有属性
#执行name长度大于20的字串，进行操作
#重复元素，操作
def  click_elements_one(names,act,number=20):
	global driver
	#当前操作
	cur_act={}
	#返回的操作存放
	cur_acts=[]
	#print(t)
	#提取属性id,name,classname
	t=[]
	t_value=[]
	for  i in range(len(names)):
		t.append(names[i][3])
		if act=="text":			
			t_value.append(names[i][3]['text'])
		elif act=="id":
			t_value.append(names[i][3]['resource-id'])
		else:
			t_value.append(names[i][3]['class'])

	#-------------------------------
	#1菜单 排除menu
	names_temp=exclude_menu(t_value)

	#2调用重复，有重复进行操作
	names_temp=repeat_elements_clicks(t_value,act)

	#执行其他操作
	#统计次数
	n=0
	ac = get_current_activity()
	for i in range(len(names_temp)):
		print('正在执行%s,第%d-------------------------'%(act,i+1))
		#print(names[i])
		#只返回一个值时用

		#反着执行
		t=names_temp[len(names_temp)-i-1]

		#t=names[i]
		#按text进行操作
		if act=='text':
			#text长度<=字符数，进行点击
			if len(t)<=number:
				print('执行%s---'%act,t)			
				#输入框时，输入内容
				#method=""
				method=is_edit(t)
				#调用操作

				click_all(t,act,method)
				'''
				#取bounds值
				#反着查找，因为删除了重复了
				t_bounds=[]
				for i in range(len(t)):		
					temp=t[len(t)-i-1]
					print(t[len(t)-i-1])
					temp_value=t[len(t)-i-1]['text']
		
					if t==temp_value:
						t_bounds.append(temp["bounds"])
						break
				print(len(t))
				'''
				if t=="书架":
					#关闭弹窗，点击返回
					#tanchuang(huodong)
					tanchuang_all()
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

#判断是否有重复,有重复进行操作，然后删除重复，返回删除后
def repeat_elements_clicks(names,act):
	global driver
	#存放names
	temp_names=names
	#存放重复值
	repeat_element=[]
	flag=False
	print('去重复前--------------',len(names),names)
	for i in range(len(names)):
		#倒序执行
		t=names[len(names)-i-1]

		#取当前元素		
		#t=names[i]
		#print('当前----------------',i,t)

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
	if len(repeat_element)>0:
		print('重复----------------------',repeat_element)
		for x in repeat_element:
			for i in range(len(names)):
				if x in names:
					temp_names.remove(x)
			print('已去除重复',x)
	
	#names删除后
	names=temp_names
	print('去重复后--------------',len(names),names)		
	
	return names

#判断操作是否是输入框，是返回edit,id
def is_edit(t):
		#输入框时，输入内容
		#edit_include 配置输入框值
		if t in edit_include:
			method="edit"
		else:
			method=""
		return method


#元素组的进行操作，id,name,class,
def count_element(names,e,act):
	global driver
	ac=get_current_activity()
	count=names.count(e)
	#当有多个一样的值是，执行find_elements
	el_counts=[]
	if count>1:
		try:
			if act=='id':
				el_counts=driver.find_elements_by_id(e)
			elif act=="text":
				el_counts=driver.find_elements_by_name(e)
			elif act=='class':
				el_counts=driver.find_elements_by_class_name(e)
			elif act=="xpath":
				el_counts=driver.find_elements_by_xpath(e)
			else:
				print('没有此方法',act)
				
			#存在多个元素
			if el_counts:
				print('存在多个----------------------------',e)
				#print('----------------------------',el_counts)
				for i in range(len(el_counts)):
					print('正在点击多个%s,第%d个--------'%(act,i+1),e)				
					#判断是否是输入框
					method=""
					method=is_edit(el_counts[i])
					#是输入框
					click_all(el_counts[i],act,method)
				
					#el_counts[i].click()

					#判断页面是否跳转
					new=get_current_activity()
					is_new_activity(ac,new)

			return True
		except:
			return False
	else:
		return 	False


#判断操作,底部菜单
def   click_menu(t):
		global driver
		curent_menu=""
		if t=="书架":
			#关闭弹窗，点击返回
			#tanchuang(huodong)
			#tanchuang(huodong)
			tanchuang_all()
		elif t in ["书架","分类","书城","我的"]:

			if "Main2Activity" in now:

				print('点击菜单操作---------------------')

#判断不是当前菜单，点击back

#---------------------------------------------------------------------
#中间点击,tap((x1,y1),(x1,y2)],100),100毫秒
def tap_center():
	global driver
	s= getSize()
	print(s[0],s[1])
	x1 = int(s[0] * 0.5)
	y1 = int(s[1] * 0.4)
	print('x1=%s,y1=%s'%(x1,y1))
	driver.tap([(x1,y1),(x1,y1)],100)


#---------------------------------------------------------------------
#判断是否新页面，是则返回
#1.跳转到有活动弹窗的，点击关闭
#2.跳转到搜索页，返回2次
#3.跳转到阅读器器，返回，并点击确定
#4.阅读器中，点击打开设置
#5.搜索页

def is_new_activity(ac,new):
		global driver

		#如果跳转到了，搜索，就返回2次，跳转到阅读器，返回时判断是否有加入书架的弹窗，有就点确定	
		if ac!=new:
			print("跳转到其他页面了",new,'正在返回-----')
			#如果跳转到其他页面，返回
			driver.back()
			new=get_current_activity()
			print('new------',new)
			#返回时判断书架是否有弹窗，有则关闭
			#tanchuang(huodong)
			tanchuang_all()
			#跳转到，阅读器，返回
			if  "ReaderActivity" in  new:
				#有弹窗，点击确定，取消
				click_all("确定","text")
			#跳转到搜索，返回2次
			if "SearchActivity" in new:
				driver.back()
			print("已返回")
		

		#搜索1级，2级页面点击时，返回
		elif "SearchActivity" in   ac:
				#driver.back()
				print("在搜索页，已返回")
				pass

		#当前在阅读器中
		if "ReaderActivity" in ac:
			#点击中间，打开设置菜单
			print('当前在阅读中')
			#判断元素不存在
			name="语音朗读"
			flag=is_element_exist(name)
			#设置没有打开，就点击一次打开
			if flag=="false":
				driver.tap([(500,500),(1065,208)],100)

#判断元素是否存在，text
def is_element_exist(name):
        try:
            #el = driver.find_element_by_android_uiautomator("text(\"%s\")" %name)
            xpath_value='//*[contains(@text, %s)]'%name
            el=driver.find_element_by_xpath(xpath_value)
            return True
            print("元素定位成功")
       
        except BaseException as e:
            print(e.args)
            print("元素定位失败")
            return False



#获取当前页面的pagesource，并执行操作
def  getsource_clicks(name):
	global num
	global driver
	#
	num=num+1
	#获取当前页面pagesource
	r=get_pagesource()
	#ac = get_current_activity(driver)
	#存储文件名
	filename=pageDir+"%s_page_%s.xml"%(name,num)
	print("保存文件：",filename)
	#调用函数--------------------------------------
	#re=source_clicks_one(r,filename)
	ac = get_current_activity()
	#如果source 不为空
	if len(r)>10:

			#先将source写入xml文件中
			common.write_xml_to_file(filename,r)
			#从xml中取text，resource-id,属性元素
			names,ids,others=common.getAttrib_of_all(filename)

			#如果取值不为空
			if len(names)>0:
				#点击name
				print('names----------------个数',len(names))
				click_elements_one(names,'text')
		
			if len(ids)>0:
				#点击id
				print('ids------------------个数',len(ids))
				click_elements_one(ids,'id')
		
			if len(others)>0:
				#点击classname,
				#print('other-----------------个数',len(others))
				#click_elements_onenew(others,'class')
				pass
		
			#print('操作了id %d次')

	return len(names),len(ids),len(others)
