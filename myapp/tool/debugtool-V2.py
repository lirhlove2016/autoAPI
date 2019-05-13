#coding=utf-8
import appium
from appium import webdriver
import time
import random
from tkinter import *
import importlib
# import yongli
import threading

#引用你需要调试的文件
#举例如下
from common import elementApp as app


# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '8.0.0'
# desired_caps['deviceName'] = 'LMX4C17A28015459'
# desired_caps['appPackage'] = 'com.dzmf.zmfxsdq'
# desired_caps['appActivity'] = 'com.dzbook.activity.SplashActivity'
# desired_caps['newCommandTimeout'] = '200'
# desired_caps['automationName'] = 'UiAutomator2'

#定义你的设备信息
app.update_capability('platformName','Android')
app.update_capability('platformVersion','8.0.0')
app.update_capability('deviceName','LMX4C17A28015459')
app.update_capability('appPackage','com.aikan')
app.update_capability('appActivity','com.dzbook.activity.LogoActivity')
app.update_capability('automationName','UiAutomator2')

#引用你要调试的文件中的driver
app.start('http://localhost:4723/wd/hub',30)

driver = app.driver

def RELINK():
    global driver
    driver = app.driver

#引用xxx.py文件后，若要使用里面的方法
#举例如下
#xxx.方法()

def TD(func,*args):
    td = threading.Thread(target=func,args=args)
    td.start()


def LOOP():
    a = N1.get()
    if a == '':
        a = 1
    a = int(a)
    while a > 0:
        print(driver.page_source)
        time.sleep(3)
        a = a - 1
        # return a

def findItem():
    source = driver.page_source
    el = N3.get()
    if el == '':
        print("请输入有效内容")
    else:
        el = el.split(',')
        print("正在查找“"+el[0]+"”元素")
        # print(len(el))
        if len(el) == 1:
            if  el[0] in source:
                print(el[0]+"-存在,共" + str(source.count(el[0])) + "个")
            else:
                print(el[0] + "-不存在")
        elif len(el) > 1:
            print("正在查找这"+str(len(el))+"项元素")
            for e in el:
                if e in source:
                    print(e + "-存在，共" + str(source.count(e)) + "个")
                else:
                    print(e + "-不存在")



def P_CONTEXT():
    print(driver.current_context)



def C_FANC1():
    func = N51.get()
    R = N52.get()
    func = eval(func)
    if len(R) == 0:
        func()
    else:
        R=R.split(',')
        func(*R)

def C_FANC2():
    func = N61.get()
    R = N62.get()
    func = eval(func)
    if len(R) == 0:
        func()
    else:
        R=R.split(',')
        func(*R)

def C_FANC3():
    func = N71.get()
    R = N72.get()
    func = eval(func)
    if len(R) == 0:
        func()
    else:
        R=R.split(',')
        func(*R)



def RELOAD():
    rl = N8.get()
    print(rl)
    rl = eval(rl)
    importlib.reload(rl)

#获取尺寸
def SIZE():
    global start_x,start_y,end_x,end_y
    start_x = 0
    start_y = 0
    end_x = driver.get_window_size()['width']
    end_y = driver.get_window_size()['height']
    return (start_x,start_y,end_x,end_y)

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




top = Tk()
top.wm_title("appium 调试小工具")



B1 = Button(top,text = "连续获取source",command = lambda:TD(LOOP),width = 15).grid(row = 0,column = 0)
L1 = Label(top,text = "请输入连续获取次数，默认是1：",width = 30).grid(row = 0,column = 1)
N1 = Entry(top,width = 30)
N1.grid(row = 0,column = 2)

B2 = Button(top,text = "随机点击",command = RC,width = 15).grid(row = 1,column = 0)

B3 = Button(top,text = "查找元素",command = findItem,width = 15).grid(row = 2,column = 0)
N3 = Entry(top,width = 30)
N3.grid(row = 2,column = 1)

B4 = Button(top,text = "获取context",command = P_CONTEXT,width = 15).grid(row = 3,column = 0)


B5 = Button(top,text = "调用方法I",command = C_FANC1,width = 15).grid(row = 4,column = 0)

N51 = Entry(top,width = 30)
N51.grid(row = 4,column = 1)

N52 = Entry(top,width = 30)
N52.grid(row = 4,column = 2)



B6 = Button(top,text = "调用方法II",command = C_FANC2,width = 15).grid(row = 5,column = 0)

N61 = Entry(top,width = 30)
N61.grid(row = 5,column = 1)

N62 = Entry(top,width = 30)
N62.grid(row = 5,column = 2)



B7 = Button(top,text = "调用方法III",command = C_FANC3,width = 15).grid(row = 6,column = 0)

N71 = Entry(top,width = 30)
N71.grid(row = 6,column = 1)

N72 = Entry(top,width = 30)
N72.grid(row = 6,column = 2)


B8 = Button(top,text = "重载模块",command = RELOAD,width = 15).grid(row = 7,column = 0)

N8 = Entry(top,width = 30)
N8.grid(row = 7,column = 1)


top.mainloop()
