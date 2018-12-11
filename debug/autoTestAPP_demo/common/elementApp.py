#coding:utf-8
from appium import webdriver
import time,os

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

  
#保存元素
elements={}

#保存上一个操作的元素定位
e=""

#保存值
saveValue={}

#url
url="http://localhost:4723/wd/hub"
timeout=5
driver=""

#设备参数
desired_caps = {
            'platformName': 'Android',
            'deviceName':'722347d6', #6EB0217518004226  #722347d6
            'platformVersion': '6.0',
            #'app': PATH(r'E:\download\385.apk'), #安装目录
            'appPackage': 'com.ishugui',  
            'appActivity': 'com.dzbook.activity.LogoActivity',
            #'unicodeKeyboard': True,  #是使用unicode编码方式发送字符串
            #'resetKeyboard': True,      #隐藏键盘            
            #'noReset':True, #在会话前是否重置app状态。默认是false
            #'fullReset':'true',  #
            #'autoLaunch'：'false',  #Appium是否要自动启动或安装app，默认true
            #'newCommandTimeout':1800 #设置未接收到新命令的超时时间，默认60s,
        }


#配置设备
def update_capability(key,value):
    global desired_caps
    desired_caps[key]=value


#启动设备
def start(adddress,time):
    global url,timeout,driver
    url=adddress
    timeout=time
    
    driver = webdriver.Remote(url, desired_caps)
    driver.implicitly_wait(timeout)


   
#定位元素：index,取一组中[] name保存的命       
def get_element(method,element,index="",name=""):
    global elements,driver
    global e
    print('定位---%s------%s-----'%(method,element))


    if method=="id":
        e=driver.find_element_by_id(element)       
    elif method=="class":
        e=driver.find_element_by_class_name(element)

    elif method=="css":
        e=driver.find_element_by_css_selector(element)

    elif method=="xpath":
        e=driver.find_element_by_xpath(element)

    elif method=="name":
        e=driver.find_element_by_name(element)

    elif method=="linktext":
        e=driver.find_element_by_link_text(element)

    elif method=="text":
        new='new UiSelector().text(\"'+element+'\")'        
        e=driver.find_element_by_android_uiautomator(new)


    print('定位元素--------------------------')
    print('e:',e)
    
    if name!="":
        elements[name]=e

#操作集合
def clicks(act,element,value="",name=""):
    global elements,driver
    global e
    print('正在执行点击操作--------------------------')
    print(element)

    #不为空，提取保存的值；为空点击上一个定位元素
    if element!="":
        el=elements[element]
    else:
        el=e
    print('点击的元素是：%s-------------------------'%el)

    #根据act执行不同到操作
    if act=="click":
        result=el.click()
    elif act=="clear":
        result=el.clear()
    elif act=="input":
        result=el.send_keys(value)

    #name保存操作
    if name!="":
        saveValue[name]=result

#获取当前页所有元素
def get_pages_source():
    global elements,driver
    sources=driver.find_element_by_xpath("//*")
    
    

#操作click
def click(element,value="",name=""):
    global elements,driver
    global e
    print('正在执行点击操作--------------------------')
    print(element)

    #不为空，提取保存的值；为空点击上一个定位元素
    if element!="":
        el=elements[element]
    else:
        el=e
    print('点击的元素是：%s-------------------------'%el)
    
    result=el.click()

    #name保存操作
    if name!="":
        saveValue[name]=result


#操作clear
def clear(element,value="",name=""):
    global elements,driver
    global e
    print('点击clear--------------------------')
    print(element)
    print(e,elements)

    el=elements[element]
    print('点击的元素-------------------------',el)
    
    if element!="":        
        result=elements[element].click()           
    else:
        result=e.click()
        
    if name!="":
        saveValue[name]=result
         
#操作sendkeys
def sendkeys(element,value="",name=""):
    global elements,driver
    global e
    print('sendkeys--------------------------')
    print(element)
    print(e,elements)

    el=elements[element]
    print('输入的元素-------------------------',el)
    
    if element!="":        
        result=elements[element].send_keys(value)            
    else:
        result=e.send_keys(value)        

    if name!="":
        saveValue[name]=result        


         
#assertequals
def assertequals(key,value):
    global elements,driver
    global e
 
    print('正在校验------------------------------------')
     
    #如果有取值就用保存的参数
    
    value=re_compile(value)        
    print("realresult is %s. the expectedreslut id %s."%(jsonStr,value))

    if key.startswith('{{'):
        key=saveValue[key]
    
        
    if key==value:
        print('校验结果是 PASS')
        writer.write(reader.rr-1,7,'PASS')
        writer.write(reader.rr-1,8,value)
        
    else:
        print('校验结果是 Fail')
        writer.write(reader.rr-1,7,'Fail')
        writer.write(reader.rr-1,8,value)

               
#滑动
def swip(method,num):
    num=int(num)
    i=0   
    while i <num:
        if method=="left":
            swipeLeft()
        elif method=="right":
            swipeRight()            
        i=i+1

#scroll
def scroll(ori_el,des_el):
    global elements,driver
    deriver.scroll(ori_el,des_el)
        
#scroll
def current_context():
    global driver
    driver.current_context


#获得所有contexts
def contexts():
    global driver    
    driver.contexts


#sleep
def sleep(t):
    global driver
    t=int(t)    
    time.sleep(t)


#保存图片到本文件夹,暂时不用
def save_screenshot(filename):
    global driver
    driver.save_screenshot(filename)


#保存图片到指定文件夹
def get_screenshot(filepath,filename):
    global driver
    filename=filepath+filename
    print('------------------------------保存图片',filename)
    driver.get_screenshot_as_file(filename)


    
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


if __name__=="__main__":

    #update_capability("appPackage","diankan")
    print(desired_caps)

