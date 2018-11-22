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
            #'resetKeyboard': 'True'   
            #'unicodeKeyboard': 'True',  
            #'noReset':'true', #不清数据
            #'fullReset':'true',  #保留账号
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

    if name!="":
        elements[name]=e
        
    print(method,element)
    print('定位元素--------------------------')
    print('elements[%s]'%(name),elements[name],'e:',e)


#操作
def click(act,element,value="",name=""):
    global elements,driver
    global e
    print('点击click--------------------------')
    print(act,element)
    print(e,elements)

    el=elements[element]
    print('点击的元素-------------------------',el)
    
    if act=="click":
        if element!="":        
            result=elements[element].click()
            
        else:
            result=e.click()
        
    if name!="":
        saveValue[name]=result
         
      
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

#sleep
def sleep(time):
    time.sleep(time)
    
        
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

