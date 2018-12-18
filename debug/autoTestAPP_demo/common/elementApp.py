# coding:utf-8
from appium import webdriver
import time, os
from common import readexcel as reader, writeexcel as writer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.conf import dataDir, reportDir

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

# 保存图片
resultfile = os.path.join(reportDir, 'screenshot/screenshot_')
number = 0  # 保存图片序号用

# 保存元素
elements = {}
# 保存上一个操作的元素定位
e = ""
# 保存值
saveValue = {}
# url
url = "http://localhost:4723/wd/hub"
timeout = 30
driver = ""


# 写入结果
def wirte_result(result, value):
    if reader.rr>0:
        writer.write(reader.rr - 1, 7, result)
        writer.write(reader.rr - 1, 8, value)

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

#输入中文内容前调用
def input_before():
    if  desired_caps['unicodeKeyboard']==False:
        desired_caps['unicodeKeyboard']=True

    if  desired_caps['resetKeyboard']==False:
        desired_caps['resetKeyboard']=True

    print(desired_caps['unicodeKeyboard'])
    print(desired_caps['resetKeyboard'])

#输入中文内容后调用
def input_after():
    if desired_caps['unicodeKeyboard']==True:
        desired_caps['unicodeKeyboard']=False

    if desired_caps['resetKeyboard']==True:
        desired_caps['resetKeyboard']=False

    print(desired_caps['unicodeKeyboard'])
    print(desired_caps['resetKeyboard'])

    
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
        print('启动失败了', err)
        print('请检查是否启动appium')
        rerun(start,adddress, t)


# 定位元素：index,取一组中[] name保存值
def get_element(method, element, index="", name="", casename=""):
    global elements, driver
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

        elif method == "name":
            e = driver.find_element_by_name(element)

        elif method == "linktext":
            e = driver.find_element_by_link_text(element)

        elif method == "text":
            new = 'new UiSelector().text(\"' + element + '\")'
            e = driver.find_element_by_android_uiautomator(new)

        print('定位元素--------------------------')
        print('e:', e)
        # 写入信息
        re = "PASS"
        value = element

        if name != "":
            elements[name] = e
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
    global elements, driver
    global e
    global number

    print('正在执行%s操作--------------------------' % act)
    print(element)
    # 不为空，提取保存的值；为空点击上一个定位元素
    if element != "":
        el = elements[element]
    else:
        el = e
    print('操作的元素是：%s-------------------------' % el)
    try:
        # 根据act执行不同到操作
        if act == "click":
            result = el.click()
        elif act == "clear":
            result = el.clear()
        elif act == "input":
            #input_before()
            value=str(value)            
            result= el.send_keys(value)
            print('正在输入内容',value)

            #input_after()
            
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
def sleep(t):
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
        wirte_result("PASS", filename)

    except Exception as err:
        #调用方法
        err_run(err,get_screenshot,filepath,file)
        
#---------
# 保存图片到本文件夹,暂时不用
def save_screenshot(filename):
    global driver
    driver.save_screenshot(filename)
    # 写入
    wirte_result("PASS", filename)

# 获取当前页所有元素
def get_pages_source():
    global elements, driver
    sources = driver.find_element_by_xpath("//*")

# scroll
def scroll(ori_el, des_el):
    global elements, driver
    deriver.scroll(ori_el, des_el)

# current_context
def current_context():
    global driver
    driver.current_context

# 获得所有contexts
def contexts():
    global driver
    driver.contexts


'''
# 滑动
def swiptest(method, num):
    num = int(num)
    i = 0
    while i < num:
        if method == "left":
            swipeLeft()
        elif method == "right":
            swipeRight()
        elif method == "up":
            swipeUp()
        elif method == "down":
            swipeDown()
        i = i + 1

    # 写入
    value = method + ":" + str(num)
    wirte_result("PASS", value)


# 获取屏幕宽度和高度
def getSize():
    global driver
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 向左滑动
def swipeLeft():
    global driver
    s = getSize()
    x1 = int(s[0] * 0.8)
    y1 = int(s[1] * 0.5)
    x2 = int(s[0] * 0.2)
    driver.swipe(x1, y1, x2, y1)
'''

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

if __name__ == "__main__":
    pass
