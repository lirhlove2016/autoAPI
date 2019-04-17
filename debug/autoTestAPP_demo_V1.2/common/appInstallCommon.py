#!/usr/bin/env python
#coding=utf-8

import os
import platform
import subprocess
import re
from time import sleep
from conf  import conf
from common import elementApp as app


"""
封面安装包相关
1.安装包
2.卸载包
3.获取包名
4.执行操作

"""

#------------------------------------------------------    
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

#------------------------------------------------------  
#app包目录获取
def get_app_filelist(appfilepath):
    global L
    L = []
    for x1, x2, x3 in os.walk(appfilepath):
        x3 = str(x3)
        if x3 != '[]':
            x3 = x3.split(',')
            x3 = list(x3)
            n = 0
            for p in x3:
                z = x3[n].replace("'", "")
                z = z.replace("]", "")
                z = z.replace("[", "")
                z = z.replace(" ", "")
                n = n + 1
                # print(os.path.join(x1, z))
                L.append(os.path.join(x1, z))
    return L	

#------------------------------------------------------    
def install_appPackage(apppath):
        '''
        安装apppath下的app包      
        '''
        cmd='adb install %s'%apppath
        out = os.popen(cmd).read()

        if 'Success' in out:
            print('success，app包安装成功了！',)
        else:
            #获取失败原因
            msg=out[out.find("Failure"):]                 
            print('安装失败，请检查是否连接设备，是否已经安装。',msg)

            #失败时重试3次
            #rerun(install_appPackage,apppath)
            

#------------------------------------------------------        
def uninstall_apppackage(packname):
        '''
        卸载app包      
        '''
        global pack        
        #packname为空时取配置参数值
        if packname=="":
            packname=pack
            
        cmd='adb uninstall %s'%packname
        out = os.popen(cmd).read()        
        if 'Success' in out:
            print('success，%s app包已经卸载了！'%packname)

        else:      
            print('卸载失败，请检查是否连接设备。包名%s，失败原因%s'%(packname,out))
            #失败时            
            packname,activity=get_package()
            if packname==False:
                #失败时重试3次
                rerun(get_package)
                print('获取包失败，不能卸载！')

            #失败时重试3次
            rerun(uninstall_apppackage,packname)

        # 写入
        app.wirte_result('PASS',"pack："+packname+"activity:"+activity)


#-------------------------------------
def  install_app_run(applist,method=0,radio=0.3):
    '''
    applist:app包目录
    interval：0每个包都安装，正整数为间隔1隔安装,负值按比例安装
    radio:默认30%安装
    '''
    #存放app包数量
    total=len(applist)
    print('---------------------------------------------------------')
    print('总包数量 ',total)
    print('---------------------------------------------------------')
    #num为0，都安装
    if method==0:
        #安装数量
        i=1
        print('当前安装模式顺序安装')
        print('---------------------------------------------------------')
        for apppath in applist:
            
            #调用执行操作
            execute_run(i,apppath)
            i=i+1
                                    
    #大于0，间隔安装
    elif method>=1:
        #间隔n个安装
        interval=method+1
        print('当前安装模式跳着安装')
        print('---------------------------------------------------------')
        i=0  #计数
        j=1  #安装包计数
        for x in  applist:    
            #运行安装
            apppath=applist[i]
            #调用执行操作            
            execute_run(i+1,apppath)
            
            i=i+interval
            if i <total:
                continue
            else:
                break        
  
    #负数,按radio取百分比安装
    elif method<0:  
        print('当前安装模式按比例%s安装'%(radio*100))
        print('---------------------------------------------------------')
        if radio >0 and radio <1:
            #需安装的个数
            num=int(total*radio)
            print('需要安装包的数:',num)
            #安装包顺序
            p=int(total/num)
            i=0  #计数
            temp=1  #已经安装的包数
            for x in  applist:    
                apppath=applist[i]
                
                #调用执行操作
                execute_run(i+1,apppath)
                temp=temp+1
                i=i+p
                #已安装的包数判断
                if i <total and  temp<=num:
                    continue
                else:
                    break
        else:
            print('比例错误，请确认！！！')

#-------------------------------------    
def get_package():
    
    #打开app,启动
    #获取包名和启动页
    print('正在获取包名，请打开app')
    print('---------------------------------------------------------')
    input('如果已经打开app，按任意键继续....\n')

    pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")    
    out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read() 
    out_list = pattern.findall(out)
    print(out_list)
    
    if len(out_list)>=1:
        component = out_list[0] #输出列表中的第一条字符串
        component=str(component )

        res=component.split('/')
        pack=res[0]        
        activity=res[1]
        print("package="+pack+'\n'+"activity="+activity) 
        #print("package="+pack+'\n')        
        #返回2个值    
        print('---------------------------------------------------------')

        #写入conf
        conf.appPackage=pack
        conf.appActivity=activity
        print('存到conf中',conf.appPackage,conf.appActivity)
        return pack,activity

    elif len(out_list)==0:
        print('包名为空，请确认下是否已经安装了app。')
        #失败时重试3次
        rerun(get_package)               
        return False
    else:
        print('无法获取包名，请确认下是否已经安装了app。')
        return False


    
#------------------------------------------------------------------------------
def execute_run(i,apppath):    
            print("正在安装第%d个包:%s"%(i,apppath))
            #安装
            install_appPackage(apppath)
            #执行例检
            print('---------------------------------------------------------')
            print('正在执行例检，请稍等....')
            print('---------------------------------------------------------')
            re=input('已经执行完成，请按任意键继续..........\n')            
            
            #卸载前先获取包名
            packname,activity=get_package()
            

            input('即将执行卸载，请按任意键继续....\n')
            uninstall_apppackage(packname)
            print('---------------------------------------------------------')

#------------------------------------------------------------------------------
        
if  __name__=='__main__':
    pass
    


    



