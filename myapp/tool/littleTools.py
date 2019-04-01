#-*-coding:utf-8-*-
import os
from tkinter import *

root=Tk()
root.title('小工具')


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


#输入命令
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


#命令行
#b1=Button(root,text="点击看看吧",command=show,height=1,width=15,fg='blue').grid(row=2,column=1)    
#Label(root, text='显示结果', width=15, height=1).grid(row=2,column=1,sticky=W) #靠左

b1=Button(root,text="执行命令",command=get_text,height=1,width=15,fg='blue').grid(row=0,column=2,padx=5, pady=5)
b2=Button(root,text="安装包",command=show,height=1,width=15,fg='blue').grid(row=1,column=2,padx=5, pady=5)

b3=Button(root,text="查看设备",command=get_app_deviceid,height=1,width=15,fg='blue').grid(row=4,column=0,padx=5, pady=5)
b4=Button(root,text="清空",command=clear,height=1,width=15,fg='black').grid(row=4,column=2,padx=5, pady=5)


#显示结果text
text = Text(root, width=30, font =('Verdana',10),fg='blue')
text.grid(row=4,column=1,rowspan=3)


root.mainloop()






