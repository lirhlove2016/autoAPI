#coding:utf-8
from appium import webdriver
import time,os
from common import readexcel as reader,writeexcel as writer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from conf.conf import dataDir,reportDir
#exe
from conf.conf_exe import dataDir,reportDir

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

#保存图片 
resultfile=os.path.join(reportDir,'screenshot/screenshot_')

#保存元素
elements={}
#保存上一个操作的元素定位
e=""
#保存值
saveValue={}
#url
url="http://localhost:4723/wd/hub"
timeout=30
driver=""

#写入结果
def wirte_result(result,value):        
        writer.write(reader.rr-1,7,result)
        writer.write(reader.rr-1,8,value)
                     
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
            'noReset':False, #在会话前是否重置app状态。默认是false
            #'fullReset':'true',  #
            #'autoLaunch'：'false',  #Appium是否要自动启动或安装app，默认true
            'newCommandTimeout':60, #设置未接收到新命令的超时时间，默认60s,
            #'automationName': 'uiautomator2',       
        }

#配置设备
def update_capability(key,value):
    global desired_caps
    if key=='newCommandTimeout':
            value=int(value)
        
    desired_caps[key]=value
    #写入
    wirte_result('PASS',value)


#启动设备
def start(adddress,t):
    global url,timeout,driver
    url=adddress
    timeout=int(t)
    try:
        driver = webdriver.Remote(url, desired_caps)
        driver.implicitly_wait(timeout)

        #写入
        wirte_result('PASS',"设备已经启动,wait%d"%timeout)
    except Exception as err:
        print('启动失败了')

   
#定位元素：index,取一组中[] name保存的命       
def get_element(method,element,index="",name=""):    
    global elements,driver
    global e
    
    print('定位---%s------%s-----'%(method,element))
    try:
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
        #写入信息       
        re="PASS"
        value=element
            
        if name!="":
            elements[name]=e          

    #异常
    except Exception as err:
        print("定位报错了:",err)        
        get_screenshot(resultfile,"_error_element.png")
        #写入信息
        re="Fail"
        value=element
        
    #写入
    wirte_result(re,value)
            

#操作集合
def clicks(act,element,value="",name=""):
    global elements,driver
    global e
    
    print('正在执行%s操作--------------------------'%act)
    print(element)

    #不为空，提取保存的值；为空点击上一个定位元素
    if element!="":
        el=elements[element]

    else:
        el=e
        
    print('操作的元素是：%s-------------------------'%el)

    try:
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
        #写入值
        re="PASS"
        value="执行成功"
        
    #异常
    except Exception as err:
        print("报错了:",err)
        #写入值
        re="FAIL"
        value=element
        
    #写入
    wirte_result(re,value)

#quit
def quit():
    global driver
    driver.quit()
    #写入
    wirte_result("PASS","操作成功")      

 #back,点击返回键
def back():
    global driver
    driver.quit()
    #写入
    wirte_result("PASS","操作成功")      

#获取当前页所有元素
def get_pages_source():
    global elements,driver
    sources=driver.find_element_by_xpath("//*")
                      

#scroll
def scroll(ori_el,des_el):
    global elements,driver
    deriver.scroll(ori_el,des_el)
        
#current_context
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
    #写入
    value="等待%s"%t
    wirte_result("PASS",value)    

#保存图片到本文件夹,暂时不用
def save_screenshot(filename):
    global driver
    driver.save_screenshot(filename)
    #写入
    wirte_result("PASS",filename)    

#保存图片到指定文件夹
def get_screenshot(filepath,filename):
    global driver
    filename=filepath+filename
    print('正在保存图片',filename)
    driver.get_screenshot_as_file(filename)
    #写入
    wirte_result("PASS",filename)   

#滑动
def swiptest(method,num):
    num=int(num)
    i=0   
    while i <num:
        if method=="left":
            swipeLeft()
            
        elif method=="right":
            swipeRight()
            
        elif method=="up":
            swipeUp()
            
        elif method=="down":
            swipeDown()
        i=i+1

    #写入
    value=method+":"+str(num)
    wirte_result("PASS",value)     


    
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
        x1 = int(s[0] * 0.8)
        y1 = int(s[1] * 0.5)
        x2 = int(s[0] * 0.2)	
        driver.swipe(x1, y1, x2, y1)


#向右滑动
def swipeRight():
        global driver
        s= getSize()
        x1 = int(s[0] * 0.8)
        y1 = int(s[1] * 0.5)
        x2 = int(s[0] * 0.2)
        driver.swipe(x2, y1, x1, y1)

#向上滑动
def swipeUp():
        global driver
        s= getSize()
        x1 = int(s[0] * 0.5)
        y1 = int(s[1] * 0.2)
        y2 = int(s[0] * 0.8)
        driver.swipe(x1, y1, x1, y2)


#向下滑动
def swipeDown():
        global driver
        s= getSize()
        x1 = int(s[0] * 0.5)
        y1 = int(s[1] * 0.2)
        y2 = int(s[0] * 0.8)
        driver.swipe(x1, y2, x1, y1)        

#获取尺寸
def SIZE():
    global start_x,start_y,end_x,end_y
    start_x = 0
    start_y = 0
    end_x = driver.get_window_size()['width']
    end_y = driver.get_window_size()['height']
    return (start_x,start_y,end_x,end_y)


#上划
def UP():
    try:
        x1 = int(SIZE()[2]*0.5)
        y1 = int(SIZE()[3]*0.2)
        y2 = int(SIZE()[3]*0.8)
        driver.swipe(x1,y2,x1,y1)

    except BaseException as e:
        print(e.args)
       
#下划
def DOWN():
    try:
        x1 = int(SIZE()[2]*0.5)
        y1 = int(SIZE()[3]*0.2)
        y2 = int(SIZE()[3]*0.8)
        driver.swipe(x1,y1,x1,y2)
    except BaseException as e:
        print(e.args)
        

#左划
def LEFT():
    try:
        x1 = int(SIZE()[2]*0.2)
        x2 = int(SIZE()[2]*0.8)
        y1 = int(SIZE()[3]*0.5)
        driver.swipe(x2,y1,x1,y1)
    except BaseException as e:
        print(e.args)
       

#右划
def RIGHT():
    try:
        x1 = int(SIZE()[2]*0.2)
        x2 = int(SIZE()[2]*0.8)
        y1 = int(SIZE()[3]*0.5)
        driver.swipe(x1,y1,x2,y1)
    except BaseException as e:
        print(e.args)
      


if __name__=="__main__":
    pass


