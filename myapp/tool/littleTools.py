#-*-coding:utf-8-*-
import os
from tkinter import *

root=Tk()
root.title('执行窗口')


def add(a,b):
    a=int(a)
    b=int(b)
    sum=eval('a+b')  #执行表达式
    print('a+b=',sum)

    return sum

#调用其他函数fun(asg1,asg2)
def go_func():
    #第一个参数，调用函数，第2个参数，函数参数
    func = n51.get()
    asgs = n52.get()
    func = eval(func)  #转为函数
    #print(type(func))    
    #无参数
    if len(asgs) == 0:
        func()
    else:
        #多参数j,分割
        asg=asgs.split(',')
        func(*asg)

#--------------------------------------
#清空文本框内容
def  clear():
    text.delete('1.0','end')
    
#执行
def show():
    print('hello')
    text.insert('1.0', "hello\n")

#文本信息
def insert_text(msg):
    text.insert(INSERT,'%s'%msg)

def get_app_deviceid():    
    print('请先检查是否连接了设备，是否启动了开发者选项，是否开启了adb调试....')
    #查看连接设备
    out=os.popen('adb devices').read()
    patter= re.compile(r"[a-zA-Z0-9]+") 
    device_list=patter.findall(out)
    #print(device_list)
    print('设备连接信息:--------------------------------------\n',out)

    #调取text
    insert_text(out)
    
    #存放设备号
    deviceid=[]
    #提取设备号，存放到deviceid中，
    if 'device' in device_list:
        #print('设备号:',deviceid)
        #多个设备，
        n=4
        while len(device_list)>n:
            deviceid.append(device_list[n])
            n=n+2
        print('设备号:',deviceid)        
    else:
        print('无此设备，请检查是否连接设备。')
    return out


#执行cmd命令
def  execute_cmd(cmd='adb devices'):
        cmd= e1.get()
        print(cmd)
        out = os.popen(cmd).read()
        print(out)
        return out

def get_text():
    # 获取entry输入的文字
    str2=""
    str2=e1.get()
    
    # 在光标处插入文字
    text.insert("insert", str2)
    
#-grid-----------------------------------------------------------------------

#label控件
Label(root,text="输入命令:").grid(row=0,column=0,sticky=E) #靠右
Label(root,text="本地目录:").grid(row=1,column=0,sticky=E) #靠右
Label(root, text='手机目录').grid(row=2,column=0,sticky=E) #靠左

Label(root, text='显示结果',width=15).grid(row=3,column=1,sticky=W) #靠左

#输入控件
e1=Entry(root,width=30)
e1.grid(row=0,column=1,padx=5,pady=5)
e2=Entry(root,width=30)
e2.grid(row=1,column=1,padx=5,pady=5)
e3=Entry(root,width=30)
e3.grid(row=2,column=1,padx=5,pady=5)


#命令控件
#b1=Button(root,text="点击看看吧",command=show,height=1,width=15,fg='blue').grid(row=2,column=1)    
#Label(root, text='显示结果', width=15, height=1).grid(row=2,column=1,sticky=W) #靠左
#grid(row=1,column=2),row,行，从0开始，column列从0开始；
b1=Button(root,text="执行命令",command=get_text,height=1,width=15,fg='blue').grid(row=0,column=2,padx=5, pady=5)
b2=Button(root,text="安装包",command=show,height=1,width=15,fg='blue').grid(row=1,column=2,padx=5, pady=5)

b3=Button(root,text="查看设备",command=get_app_deviceid,height=1,width=15,fg='blue').grid(row=4,column=0,padx=5, pady=5)
b4=Button(root,text="清空",command=clear,height=1,width=15,fg='black').grid(row=4,column=2,padx=5, pady=5)



#显示结果，text控件
text = Text(root, width=30, font =('Verdana',10),fg='blue')
text.grid(row=4,column=1,rowspan=3)


#调用函数
Label(root, text='调用函数').grid(row=8,column=0) 
Label(root, text='输入函数名').grid(row=8,column=1) 
Label(root, text='输入参数').grid(row=8,column=2) 

#调用函数
b5= Button(root,text = "加法",command = go_func,width = 15).grid(row = 9,column = 0,padx=5, pady=5)
#输入函数名
var1 = StringVar()
n51 = Entry(root,width = 30,textvariable = var1)
var1.set("add")
n51.grid(row = 9,column = 1)

#输入函数参数
var2 = StringVar()
n52 = Entry(root,width = 30,textvariable = var2)
var2.set("a,b")
n52.grid(row = 9,column = 2)


root.mainloop()






