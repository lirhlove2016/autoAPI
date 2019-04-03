#!/usr/bin/env python
#coding=utf-8

import os
import platform
import subprocess
import re
from time import sleep


"""
1.install_app_run

"""


#app包目录获取
def get_app_filelist(strlj):
    global L
    L = []
    for aaa, bbb, ccc in os.walk(strlj):
        ccc = str(ccc)
        if ccc != '[]':
            ccc = ccc.split(',')
            ccc = list(ccc)
            n = 0
            for CCC in ccc:
                zz = ccc[n].replace("'", "")
                zz = zz.replace("]", "")
                zz = zz.replace("[", "")
                zz = zz.replace(" ", "")
                n = n + 1
                # print(os.path.join(aaa, zz))
                L.append(os.path.join(aaa, zz))			
    return L	

#------------------------------------------------------    
def install_appPackage(apppath):
        '''
        安装apppath下的app包      
        '''
        cmd='adb install %s'%apppath
        out = os.popen(cmd).read()

        if 'Success' in out:
            print('success，app包安装成功了！')
        else:
            print('安装失败，请检查是否连接设备，是否已经安装。')

#------------------------------------------------------        
def uninstall_apppackage(packname):
        '''
        卸载app包      
        '''
        cmd='adb uninstall %s'%packname
        out = os.popen(cmd).read()        
        if 'Success' in out:
            print('success，app包已经卸载了！')
        else:
            print('卸载失败，请检查是否连接设备。')



#-------------------------------------
def  install_app_run(applist,interval=0,radio=0.3):
    '''
    applist:app包目录
    interval：0每个包都安装，正整数为间隔1隔安装,负值按比例安装
    radio:默认30%安装
    '''
    #存放app包数量
    total=len(applist)
    #num为0，都安装
    if interval==0:   
        print('当前安装模式顺序安装') 
        for apppath in applist:
            print(apppath)
            #install_appPackage(apppath)        
            #运行安装
                       
    #num大于0，间隔安装
    elif interval>0:
        print('当前安装模式跳着安装') 
        i=1  #计数
        for x in  applist:    
            #运行安装
            apppath=applist[i]
            print(i)
            install_appPackage(apppath)
            i=i+interval
            if i <total:
                continue
            else:
                break        
  
  #负数,按radio取百分比安装
    elif interval<0:  
        print('当前安装模式按%s安装'%(radio))
        if radio >0 and radio <1:
            num=int(total*radio)
            print(total,num)
            #需安装的个数
            p=int(total/num)
            i=1  #计数
            for x in  applist:    
                #运行安装
                apppath=applist[i]
                print(i+1)
                install_appPackage(apppath)
                i=i+p
                if i <total:
                    continue
                else:
                    break
        else:
            print('比例错误，请确认')

#-------------------------------------
#执行安装，安装后等待
#执行卸载，安装下一个


#-------------------------------------
def  print_info():
    print('    选择安装方式')
    print('---------------------------------------------')
    print('--0    顺序安装')
    print('--1    跳着安装（大于1以上）')
    print('--2    按比例安装（默认30%）')
    print('---------------------------------------------')

    
    flag=True
    while flag:
        choice=input('请输入安装方式编号(不输入默认0）：')
        if choice !='':          
            if choice  in ['0','1','2']:
                choice=int(choice)
                flag=False
                  
            else:
                  print('输入错误，请重新输入')
                  continue
        else:
          choice=1
          flag=False
          
    number=1
    #跳着安装
    if choice==1:
        flag=True
        while flag:
            number=input('请输入间隔数(大于1）：')

            if number  !='':
                #number=int(number)
                #判断是数字,且>1
                if  number.isdigit() and number>'1':                               
                      flag=False
                      number=int(number)
                          
                else:
                      print('输入错误，请重新输入')
                      continue
            else:
                print('输入错误，请重新输入')
                continue
        
    #按比例安装
    radio=0
    if choice==2:
        flag=True
        while flag:
            
            radio=input('请输入安装比例，如0.3（默认0.3）：')
            #radio=float(str)
            if radio !='':
                #数字或字母
                if radio.isdigit() or  radio.isalpha():
                    print('输入错误，请重新输入')
                    continue                                    
                else:                   
                    flag=False                  

            else:
                radio=0.3
                flag=False

    
    print('您选择的安装方式为:',choice)
    if number>1:
        print('间隔%d个安装'%number)
    if radio!=0:
        radio=float(radio)
        print('安装比例为',radio)    
    return choice,number,radio
    
def input_filapath():
    appfilepath=input('请输入安装包所在目录,如D:\\app：')
    return appfilepath


           
if  __name__=='__main__':
          
    re=print_info()
    #appfilepath="F:\\download"
    #F:\download
    appfilepath=input_filapath()
    #appfile=get_app_filelist(r'D:\\app')   
    print('包所在目录为：',appfilepath)
    appfile=get_app_filelist(appfilepath)
    print(appfile)

    #文件夹安装
    install_app_run(appfile,re[0],radio=0.3)
    if re[0]==1:    
        install_app_run(appfile,1,radio=0.3)
    if re[0]==2:
        install_app_run(appfile,-1,radio=re[2])

    
    
    '''      
    appfile=get_app_filelist(r'F:\download')
    
    print(appfile)
    #单个安装
    #install_appPackage(appfile[0])


          
    #文件夹安装
    #install_app_run(appfile,interval=2,radio=0.3)

    '''



    



