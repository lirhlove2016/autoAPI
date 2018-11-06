#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
import xlrd
from xlutils.copy import copy
import os

#读取需要复制的Excel
workbook=None
#拷贝的工作空间
wb=None
#当前工作的sheet
sheet=None
#记录要生成的文件，用来保存
df=None

#支持xls文件

#复制打开excel
def copy_open(srcfile,desfile):
    global workbook,wb,sheet,df

    if not os.path.isfile(srcfile):
        print(srcfile+'file not exist.')
        return
    if os.path.isfile(desfile):
        print('warning:'+desfile+"file already exist.")
    #记录要保存的文件
    df=desfile
    #读取excel
    workbook=xlrd.open_workbook(srcfile, formatting_info=True)  #formatting_info=True 保留原excel格式
    #拷贝
    wb=copy(workbook)
    #
    sheet=wb.get_sheet("Sheet1")
    return

#写入指定的单元格，保留格式
def write(r,c,value):
    global workbook
    global sheet

    #获取要写入的单元格
    def _getCell(sheet,r,c):
        #获取行
        row=sheet._Worksheet__rows.get(r)
        if not row:
            return None
        #获取单元格
        cell=row._Row__cells.get(c)
        return cell

    #获取要写入的单元格
    cell=_getCell(sheet,r,c)
    
    #写入值
    sheet.write(r,c,value)
    #指定写入的格式
    if cell:
        ncell=_getCell(sheet,r,c)
        if ncell:
            #设置写入后的格式和写入前一样
            ncell.xf_idx=cell.xf_idx
    return 

#保存
def save_close():
    global wb,df
    wb.save(df)
    return

def write_excel(filepath,datas,names):
    """写入数据"""
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)             
    sheet= f.add_sheet(u'sheet1',cell_overwrite_ok=True) 
    n=[]
    for i in range(len(names)):
        
        sheet.write(0,i,names[i])
        n.append(names[i])
   
    #写入数据
    d=[]
    for i in range(len(datas)):
        value=datas[i]
        #print("正在写入第{0}行，数据{1}".format(i+1,value)) 
        for j in range(len(names)):         
            key=names[j]
            if key=='Id':
                strValue=int(value[key])
            else:
                strValue=str(value[key])               
            sheet.write(i+1,j,strValue)       

        d.append(datas[i])                 
    f.save(filepath)
    print ("write finished")

if __name__=="__main__":
    srcfile="D:\\workdtation\\mygitwork\\project\\autoTestApi\\myHttpxls.xls"
    desfile="D:\\workdtation\\mygitwork\\project\\autoTestApi\\myHttp_result.xls"
    copy_open(srcfile,desfile)
    
    write(3,7,'PASS')
    write(4,7,'Fail')
    
    save_close()



