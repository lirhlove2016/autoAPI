#coding=utf-8
import appium
from appium import webdriver
import time
import random
from tkinter import *
import importlib
# from yongli import *

#引用你需要调试的文件
#举例如下
import yongli

#引用你要调试的文件中的driver
driver = yongli.DRIVER()

#引用xxx.py文件后，若要使用里面的方法
#举例如下
#xxx.方法()




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
    elif el in source:
        print(el+"存在")
    else:
        print(el + "不存在")

def P_CONTEXT():
    print(driver.current_context)



def C_FANC():
    func = N51.get()
    R = N52.get().split(',')
    func = eval(func)
    if len(R) == 0:
        func()
    else:
        func(*R)



def RELOAD():
    rl = N6.get()
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


B1 = Button(top,text = "连续获取source",command = LOOP,width = 15).grid(row = 0,column = 0)
L1 = Label(top,text = "请输入连续获取次数，默认是1：",width = 30).grid(row = 0,column = 1)
N1 = Entry(top,width = 30)
N1.grid(row = 0,column = 2)

B2 = Button(top,text = "随机点击",command = RC,width = 15).grid(row = 1,column = 0)

B3 = Button(top,text = "查找元素",command = findItem,width = 15).grid(row = 2,column = 0)
N3 = Entry(top,width = 30)
N3.grid(row = 2,column = 1)

B4 = Button(top,text = "获取context",command = P_CONTEXT,width = 15).grid(row = 3,column = 0)


B5 = Button(top,text = "调用方法",command = C_FANC,width = 15).grid(row = 4,column = 0)

N51 = Entry(top,width = 30)
N51.grid(row = 4,column = 1)

N52 = Entry(top,width = 30)
N52.grid(row = 4,column = 2)


B6 = Button(top,text = "重载模块",command = RELOAD,width = 15).grid(row = 5,column = 0)

N6 = Entry(top,width = 30)
N6.grid(row = 5,column = 1)


top.mainloop()
