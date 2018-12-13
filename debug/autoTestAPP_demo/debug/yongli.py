#coding=utf-8
import appium
from appium import webdriver
import random

#默认模拟器或真机配置
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = 'LMX4C17A28015459'
desired_caps['appPackage'] = 'com.dzmf.zmfxsdq'
desired_caps['appActivity'] = 'com.dzbook.activity.SplashActivity'

#设置模拟器或真机配置
def platformName(PN):
        desired_caps['platformName'] = PN
def platformVersion(PV):
        desired_caps['platformVersion'] = PV
def deviceName(DN):
        desired_caps['deviceName'] = DN
def appPackage(APK):
        desired_caps['appPackage'] = APK
def appActivity(ACT):
        desired_caps['appActivity'] = ACT

#启动
def DRIVER():
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

#获取尺寸
def SIZE():
    global start_x,start_y,end_x,end_y
    start_x = 0
    start_y = 0
    end_x = driver.get_window_size()['width']
    end_y = driver.get_window_size()['height']
    return (start_x,start_y,end_x,end_y)

#获取方法名称
def func_name():
    import inspect
    func_name = inspect.stack()[1][3]
    return func_name

#重试（三次）
count = 0
def rerun(func):
    global count
    count = count + 1
    if count <= 3:
        print("重试第%d次" % count)
        func()
    else:
        print("结束")
        pass
        print("结束成功")
        count = 0
        return count

#点击允许按钮
def START():
    try:
        s1 = driver.find_element_by_name("始终允许")
        s1.click()
    except BaseException as e:
        print(e.args)
        rerun(START)

#点击男生 or 女生
def NAN():
    try:
        s1 = driver.find_element_by_name("男")
        s1.click()
    except BaseException as e:
        print(e.args)
        rerun(NAN)
def NV():
    try:
        s1 = driver.find_element_by_name("女")
        s1.click()
    except BaseException as e:
        print(e.args)
        rerun(NV)

#智能等待
def DENGDAI():
    driver.implicitly_wait(10)

#点击书架视图
def SHUJIA():
    try:
        s1 = driver.find_element_by_name("书架")
        s1.click()
    except BaseException as e:
        print(e)
        rerun(SHUJIA)

#点击书城视图
def SHUCHENG():
    try:
        s1 = driver.find_element_by_name("书城")
        s1.click()
    except BaseException as e:
        print(e.args)
        rerun(SHUCHENG)

#点击分类视图
def FENLEI():
    try:
        s1 = driver.find_element_by_name("分类")
        s1.click()
    except BaseException as e:
        print(e.args)
        rerun(FENLEI)

#点击我的视图
def WODE():
    try:
        s1 = driver.find_element_by_name("我的")
        s1.click()
    except BaseException as e:
        print(e.args)
        rerun(WODE)

#上划
def UP():
    try:
        x1 = int(SIZE()[2]*0.5)
        y1 = int(SIZE()[3]*0.2)
        y2 = int(SIZE()[3]*0.8)
        driver.swipe(x1,y2,x1,y1)
    except BaseException as e:
        print(e.args)
        rerun(UP)

#下划
def DOWN():
    try:
        x1 = int(SIZE()[2]*0.5)
        y1 = int(SIZE()[3]*0.2)
        y2 = int(SIZE()[3]*0.8)
        driver.swipe(x1,y1,x1,y2)
    except BaseException as e:
        print(e.args)
        rerun(DOWN)

#左划
def LEFT():
    try:
        x1 = int(SIZE()[2]*0.2)
        x2 = int(SIZE()[2]*0.8)
        y1 = int(SIZE()[3]*0.5)
        driver.swipe(x2,y1,x1,y1)
    except BaseException as e:
        print(e.args)
        rerun(LEFT)

#右划
def RIGHT():
    try:
        x1 = int(SIZE()[2]*0.2)
        x2 = int(SIZE()[2]*0.8)
        y1 = int(SIZE()[3]*0.5)
        driver.swipe(x1,y1,x2,y1)
    except BaseException as e:
        print(e.args)
        rerun(RIGHT)

#随机点击一次
def RC():
    R = []
    for i in 'ab':
        r = random.randint(1, 10)/10
        R.append(r)
        print(R)
    x = int(SIZE()[2]*R[0])
    y = int(SIZE()[3]*R[1])
    print(str(x),str(y))
    try:
        print("即将点击" + str(x),str(y))
        driver.tap([(x,y)])
    except BaseException as e:
        print(e)
        rerun(RC)

0











