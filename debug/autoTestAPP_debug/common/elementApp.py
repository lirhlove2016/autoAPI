# coding:utf-8
from appium import webdriver
import time, os
from common import readexcel as reader, writeexcel as writer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.conf import dataDir, reportDir
from  toast import *
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


"""
实现功能
V1.0
1.定位元素
2.操作，click,clear,input
3.其他操作
4.截图
5.失败重试3次

v：1.1
1.app定位元素，批量
2.assertequals,单个元素校验
3.assertequals_all，多个元素校验
4.调用模块封装go_func()

"""

# 保存图片
resultfile = os.path.join(reportDir, 'screenshot/screenshot_')
number = 0  # 保存图片序号用

# 保存元素
elements = {}
saveelements={}
saveelements_array={}
# 保存上一个操作的元素定位
e = ""
# 保存值
saveValue = {}
# url
url = "http://localhost:4723/wd/hub"
timeout = 30
driver = ""


# 设备参数
desired_caps = {
    'platformName': 'Android',
    'deviceName': '722347d6',  # 6EB0217518004226  #722347d6
    'platformVersion': '6.0',
    # 'app': PATH(r'E:\download\385.apk'), #安装目录
    'appPackage': 'com.ishugui',
    'appActivity': 'com.dzbook.activity.LogoActivity',
    #'unicodeKeyboard': False,    #使用unicode编码方式发送字符串
    #'resetKeyboard': False,      #隐藏键盘
    #'noReset': False,         # 在会话前是否重置app状态。默认是false
    # 'fullReset':'true',
    # 'autoLaunch'：'false',     #Appium是否要自动启动或安装app，默认true
    'newCommandTimeout':1800,    #设置未接收到新命令的超时时间，默认60s,
    #'automationName': 'uiautomator2',
    #'dontStopAppOnReset': True,   # 不关闭应用
    #'autoGrantPermissions': True,  # 自动获取权限
}

# 写入结果
def wirte_result(result, value):
    if reader.rr>0:
        writer.write(reader.rr - 1, 7, result)
        writer.write(reader.rr - 1, 8, value)
    
# 配置设备
def update_capability(key, value):
    global desired_caps
    if key == 'newCommandTimeout':
        value = int(value)
    try:
        desired_caps[key] = value
        # 写入
        #wirte_result('PASS', value)

    except Exception as err:
        print(err)
        #err_run(err,update_capability,key,value)

# 启动设备
def start(adddress, t):
    global url, timeout, driver
    url = adddress
    timeout = int(t)
    try:
        driver = webdriver.Remote(url, desired_caps)
        driver.implicitly_wait(timeout)

        # 写入
        wirte_result('PASS', "设备已经启动,wait%d" % timeout)
    except Exception as err:
        print('启动失败了，错误', err)
        print('请检查是否启动appium')
        rerun(start,adddress, t)


# 定位元素：index,取一组中[] name保存值,单个元素
def get_element(method, element, index="", name="", casename=""):
    global driver
    global saveelements
    global e
    global number

    print('定位---%s------%s-----' % (method, element))
    try:
        if method == "id":
            e = driver.find_element_by_id(element)
        elif method == "class":
            e = driver.find_element_by_class_name(element)

        elif method == "css":
            e = driver.find_element_by_css_selector(element)

        elif method == "xpath":
            e = driver.find_element_by_xpath(element)
        #text    
        elif method == "name":
            e = driver.find_element_by_name(element)

        elif method == "linktext":
            e = driver.find_element_by_link_text(element)

        elif method == "partiallinktext":
            e = driver.find_element_by_partial_link_text(element)
 
        elif method=="content-desc":
            e = driver.find_element_by_accessibility_id(element)
       
        elif method == "text":
            new = 'new UiSelector().text(\"' + element + '\")'
            e = driver.find_element_by_android_uiautomator(new)

        elif method == "textContains":
            new = 'new UiSelector().textContains(\"' + element + '\")'
            e = driver.find_element_by_android_uiautomator(new)

        elif method == "textStartsWith":
            new = 'new UiSelector().textStartsWith(\"' + element + '\")'
            e = driver.find_element_by_android_uiautomator(new)         

        elif method == "textMatches":
            new = 'new UiSelector().textMatches(\"' + element + '\")'
            e = driver.find_element_by_android_uiautomator(new)  

        elif method == "resourceId":
            new = 'new UiSelector().resourceId(\"' + element + '\")'
            e = driver.find_element_by_android_uiautomator(new) 

        elif method == "resourceIdMatches":
            new = 'new UiSelector().resourceIdMatches(\"' + element + '\")'
            e = driver.find_element_by_android_uiautomator(new) 

        print('定位元素--------------------------')
        print('e:', e)
        # 写入信息
        re = "PASS"
        value = element

        if name != "":
            saveelements[name] = e

    # 异常
    except Exception as err:
        print("定位报错了:", err)
        number = number + 1
        get_screenshot(resultfile, "_error_%s_%d.png" % (casename, number))
        # 写入信息
        re = "Fail"
        value = str(err)
        #重试
        rerun(get_element,method,element,index,name,casename)

    # 写入
    wirte_result(re, value)

#定位一批元素,同单个元素定位，
def get_elements(method, element, index="", name="", casename=""):
    global driver
    global saveelements_array
    global e
    global number

    print('定位---%s------%s-----' % (method, element))
    try:
        if method == "id":
            e = driver.find_elements_by_id(element)
        elif method == "class":
            e = driver.find_elements_by_class_name(element)

        elif method == "css":
            e = driver.find_elements_by_css_selector(element)

        elif method == "xpath":
            e = driver.find_elements_by_xpath(element)
        #text    
        elif method == "name":
            e = driver.find_elements_by_name(element)

        elif method == "linktext":
            e = driver.find_elements_by_link_text(element)

        elif method == "partiallinktext":
            e = driver.find_elements_by_partial_link_text(element)
 
        elif method=="content-desc":
            e = driver.find_elements_by_accessibility_id(element)
       
        elif method == "text":
            new = 'new UiSelector().text(\"' + element + '\")'
            e = driver.find_elements_by_android_uiautomator(new)

        elif method == "textContains":
            new = 'new UiSelector().textContains(\"' + element + '\")'
            e = driver.find_elements_by_android_uiautomator(new)

        elif method == "textStartsWith":
            new = 'new UiSelector().textStartsWith(\"' + element + '\")'
            e = driver.find_elements_by_android_uiautomator(new)         

        elif method == "textMatches":
            new = 'new UiSelector().textMatches(\"' + element + '\")'
            e = driver.find_elements_by_android_uiautomator(new)  

        elif method == "resourceId":
            new = 'new UiSelector().resourceId(\"' + element + '\")'
            e = driver.find_elements_by_android_uiautomator(new) 

        elif method == "resourceIdMatches":
            new = 'new UiSelector().resourceIdMatches(\"' + element + '\")'
            e = driver.find_elements_by_android_uiautomator(new) 

        print('定位元素--------------------------')
        print('e:', e)
        # 写入信息
        re = "PASS"
        value = element

        if name != "":
            saveelements_array[name] = e

    # 异常
    except Exception as err:
        print("定位报错了:", err)
        number = number + 1
        get_screenshot(resultfile, "_error_%s_%d.png" % (casename, number))
        # 写入信息
        re = "Fail"
        value = str(err)
        #重试
        rerun(get_element,method,element,index,name,casename)

    # 写入
    wirte_result(re, value)


# 操作集合
def clicks(act, element, value="", name="", casename=""):
    global saveelements, driver
    global e
    print('正在执行%s操作--------------------------' % act)
    print(element)

    # 不为空，提取保存的值；为空点击上一个定位元素
    #调取元素
    el=get_element_of(element)

    try:
        # 根据act执行不同到操作
        if act == "click":
            result = el.click()
        elif act == "clear":
            result = el.clear()
        elif act == "input":

            value=str(value)            
            result= el.send_keys(value)
            print('正在输入内容',value)
            
        # name保存操作
        if name != "":
            saveValue[name] = result
        # 写入值
        re = "PASS"
        value = "执行成功"

    # 异常
    except Exception as err:
        print("报错了:", err)
        number = number + 1
        get_screenshot(resultfile, "_error_%s_%d.png" % (casename, number))

        re = "FAIL"
        value = str(err)
        #重试
        rerun(clicks,act,element,value, name,casename)
    # 写入
    wirte_result(re, value)

#定位元素，不为空取保存值，为空取上一个定位元素；
#引用，get_value,clicks
def get_element_of(element):
    global saveelements, driver
    global e
    #print(element)
    # 不为空，提取保存的值；为空点击上一个定
    if element != "":
        el = saveelements[element]
    else:
        el = e
    print('操作的元素是：%s-------------------------' % el)	   
    return el

#---------------------------------------------------------------
# quit
def quit():
    global driver
    try:
        driver.quit()
        # 写入
        wirte_result("PASS", "操作成功")
    except Exception as err:
        #调用方法
        err_run(err,quit)

# back,点击返回键
def back():
    global driver
    try:
        driver.back()   
        # 写入
        wirte_result("PASS", "操作成功")
    except Exception as err:
        #调用方法
        err_run(err,back)

# sleep
def sleep(t,*args,**kwargs):
    global driver
    tt = int(t)
    try:
        time.sleep(tt)
        # 写入
        value = "等待%s秒" % tt
        wirte_result("PASS", value)

    except Exception as err:
        #调用方法
        err_run(err,sleep)


# 保存图片到指定文件夹
def get_screenshot(filepath, file):
    global driver
    filename = filepath + file
    print('正在保存图片', filename)
    try:
        driver.get_screenshot_as_file(filename)
        # 写入
        wirte_result("PASS",file)

    except Exception as err:
        #调用方法
        err_run(err,get_screenshot,filepath,file)
        
#校验属性值
attributes=["resourceId","className","text","name","checkable","checked","clickable","enabled","focusable","focused","scrollable","selected"]
alls=["text","tag_name","size","loaction"]
#定位元素e获取属性，元素不为空取值，为空取上一次操作
def get_value(name,element):
	global alls,attributes
	global driver
	print('正在取值----------------------------------------------------------',name,element)
	#取定位元素属性
	el=get_element_of(element)
	print(el)

	if name in attributes:
		t=el.get_attribute(name)
		print(t)

	elif name in alls:
		if name=="text":
			t=el.text
		elif name=="tag_name":
			t=el.tag_name
		elif name=="size":
			t=el.size
		elif name=="loaction":
			t=el.location
		print(t)
	else:
		print("输入未找到：",name)
		t="fail"
	return t

#assert,name校验结果，value取值,e定位元素
def assert_equals(name,value,el):
	global driver
	print('正在进行校验-----------------------------------------------------------------')
	print('本次校验的期望结果是：%s,取值:%s'%(name,value))
	#调用取值
	values=get_value(value,el)

	#进行判断
	if name==values:
		print('校验正确,校验结果：%s'%name)
		re="PASS"
		result=name
		
	else:
		print('校验不正确，要校验的值为%s,取值:%s'%(value,values))
		re="FAIL"
		result="校验的值:"+values

	# 写入
	wirte_result(re,result)

#assert多个,
def assert_equals_all(names,values,els):
	global driver
	print('正在进行校验-----------------------------------------------------------------')	
	print('本次校验的多个期望结果是：%s,取值:%s'%(names,values))
	
	#调用拆分
	n=get_split(names)
	v=get_split(values)
	el=get_split(els)

	#依次校验每个值
	r=[]
	result=[]
	for i in range(len(n)):
		#调用取值
		values=get_value(v[i],el[i])
		#进行判断
		if n[i]==values:
			r.append("PASS")			
			result.append(n[i])
			
		else:			
			r.append("FAIL")
			result.append(values)

	#都为PASS时结果PASS,只要有一个FAIL就FAIL
	re="PASS"
	for i in range(len(re)):
		if re[i]=="FAIL":
			re="FAIL"
		
	if re!="FAIL":
		print('校验正确,校验结果：%s'%names)
	else:
		print('校验不正确，要校验的值为:%s,取值%s'%(names,result))
	
	#将result加,传给excel写入
	s=""
	for i in range(len(result)):
		s=s+result[i]+","
	print(s)
	# 写入
	wirte_result(re,s)

#拆分多个参数,以逗号拆分，去除前后空格
def  get_split(names):
	n=[]
	name=names.split(',')
	for i in range(len(name)):
		#去掉空格
		n.append(name[i].strip())
    
	return n	

#-------------------------------------------------------未调试
# 保存图片到本文件夹,暂时不用
def save_screenshot(filename):
    global driver
    driver.save_screenshot(filename)
    # 写入
    wirte_result("PASS", filename)

   
# 获取当前页元素，未可用
def get_page(*args,**kwargs):
    global  driver
    ret = driver.find_element_by_xpath(".//*")
    return ret
    
# 获取当前页所有元素
def get_pages_source(file=""):
    global driver
    
    try:       
        re=driver.page_source
        
        if file=="":
            filename="_page_%s.xml"%number
            filepath=reportDir+"_"+filename
            filepath = os.path.join(reportDir,filename)
        else:
            filepath = os.path.join(reportDir,file)
        with  open(filepath,'w+') as f:
            f.write(re)
        wirte_result("PASS", file)    
    except Exception as err:
        err_run(err,get_pages_source,filename)  
        rerun(get_pages_source,filename)

# scroll
def scroll(ori_el, des_el):
    global  driver
    deriver.scroll(ori_el, des_el)

# current_context
def current_context():
    global driver
    driver.current_context

# 获得所有contexts
def contexts():
    global driver
    driver.contexts
#-----------------------------------------------待调试

# 获取尺寸
def SIZE():
    global start_x, start_y, end_x, end_y
    start_x = 0
    start_y = 0
    end_x = driver.get_window_size()['width']
    end_y = driver.get_window_size()['height']
    return (start_x, start_y, end_x, end_y)


# 上划
def UP():
    try:
        x1 = int(SIZE()[2] * 0.5)
        y1 = int(SIZE()[3] * 0.2)
        y2 = int(SIZE()[3] * 0.8)
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
def DOWN():
    try:
        x1 = int(SIZE()[2] * 0.5)
        y1 = int(SIZE()[3] * 0.2)
        y2 = int(SIZE()[3] * 0.8)
        driver.swipe(x1, y1, x1, y2)

        value = "down"
        key = "PASS"
    except BaseException as err:
        print(err)
        value = str(err)
        key = "FAIL"

    # 写入
    wirte_result(key, value)


# 左划
def LEFT():
    try:
        x1 = int(SIZE()[2] * 0.2)
        x2 = int(SIZE()[2] * 0.8)
        y1 = int(SIZE()[3] * 0.5)
        driver.swipe(x2, y1, x1, y1)

        value = "left"
        key = "PASS"
    except BaseException as err:
        print(err)
        value = str(err)
        key = "FAIL"

    # 写入
    wirte_result(key, value)


# 右划
def RIGHT():
    try:
        x1 = int(SIZE()[2] * 0.2)
        x2 = int(SIZE()[2] * 0.8)
        y1 = int(SIZE()[3] * 0.5)
        driver.swipe(x1, y1, x2, y1)

        value = "right"
        key = "PASS"
    except BaseException as err:
        print(err)
        value = str(err)
        key = "FAIL"

    # 写入
    wirte_result(key, value)


#error时执行
def err_run(err,func,*args,**kwargs):
    print(err)
    value = str(err)
    key = "FAIL"

    # 写入
    wirte_result(key, value)
    #重试
    rerun(func,*args,**kwargs)
    

#重试（三次）
count = 1
def rerun(func,*args,**kwargs):
    global count
    if count <= 3:
        print("重试第%d次" % count)
        count = count + 1
        func(*args,**kwargs)
    else:
        print("结束成功")
        count = 1
        return count

#执行模块定义及调用---------------------------------------------------------------------------
#存放模块字典，所有可执行的模块在此存放
funcs={"caps":update_capability,
    "start":start,
    "sleep":sleep,
    "right":RIGHT,
    "left":LEFT,
    "up":UP,
    "down":DOWN,
    "element":get_element, #单个元素
    "elements":get_elements,  #一组元素 
    "clicks":clicks,       
    "savephoto":get_screenshot,
    "quit":quit,
    "back":back,
    "pagesource":get_pages_source,
    "assertequals":assert_equals,
    "assertequals_all":assert_equals_all,
    "toast":is_toast_exist, 
    "alwaysallow":always_allow,
    }



#存放定位元素和操作
ele=[["id","name","text","css","xpath","class","linktext","partiallinktext","content-desc","textContains","textStartsWith","textMatches","resourceId","resourceIdMatches"],["click","clear","input"]]
#存放定位元素组
eles=["id","name","text","css","xpath","class","linktext","partiallinktext","content-desc","textContains","textStartsWith","textMatches","resourceId","resourceIdMatches"]

#调用函数，新的模块添加到存放表中，并更新执行调用函数
def go_func(line3,line4,line5, line6,line2):    
    global funcs,ele,driver
    #函数
    name=line3
    #print("-------------------调用函数",name)    
    if name in funcs.keys():
        func=funcs[name]
        #print('执行的函数',func)
        if name in ["up","right","left","down","quit","back"]:
            func()
        elif name in ["assertequals","assertequals_all",]:
            func(line4, line5,line6)
        elif name == 'savephoto':
            func(resultfile, line4)
        elif name=='toast':
            func(driver,line4,line5,line6)
        elif name=='alwaysallow':
            func(driver,line4)
            
        else:
            func(line4, line5)

   
    #定位元素
    elif  name in ele[0]:
        func=funcs["element"]    
        #print('执行的函数',func)
        #print('正在调用定位元素---------- ',name)
        func(name, line4, line5, line6, line2)
    #操作
    elif name in ele[1]:
        func=funcs["clicks"]       
        #print('执行的函数',func) 
        #print('正在调用click操作---------- ',name)
        func(name, line4, line5, line6, line2)
    #定位一组元素
    elif name in eles:
        func=funcs["elements"]  
        #print('正在调用定位元素组---------- ',name)        
        func(name, line4, line5, line6, line2)        
    
    else:
        print('%s 不存在，请查看是否存在此模块。'%name)

#执行函数,暂时未用
def gorun(func,*args,**kwargs):
    print("重试第%d次" % count)
    func(*args,**kwargs)
#----------------------------------------------------------------------



if __name__ == "__main__":
    pass
