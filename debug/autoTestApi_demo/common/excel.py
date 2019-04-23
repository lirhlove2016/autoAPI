#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
import xlrd
from xlutils.copy import copy
import os

class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        print(self.rowNum)

    def dict_data(self):

        for x in list(range(self.colNum)):
            self.keys[0]="platform"
            self.keys[1]="menu"
            self.keys[2]="casename"
            self.keys[3]="keyword"
            self.keys[4]="arg1"
            self.keys[5]="arg2"
            self.keys[6]="arg3"
            self.keys[7]="result"
            self.keys[8]="realresult"
            
                      
        
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+1
                
                #print(s['rowNum'])
                
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
                
            return r,self.keys

    def write_excel(self,wb,datas,names,df):
        """写入数据"""
        
        sheet=wb.get_sheet("Sheet1")
        for i in range(len(datas)):
            value=datas[i]
                    
            #print("正在写入第{0}行，数据{1}".format(i+1,value)) 
            for j in range(len(names)):
                key=names[j]
                #不写入的行
                if len(value[names[0]])<1 or len(value[names[1]])<1:                    
            
                   #获取要写入的单元格，保留样式1
                    def _getCell(sheet,i,j):
                            #获取行
                            row=sheet._Worksheet__rows.get(i)
                            if not row:
                                    return None
                            #获取单元格
                            cell=row._Row__cells.get(j)
                            return cell
                    #获取要写入的单元格，保留样式2
                    cell=_getCell(sheet,i,j)

                    #写入数据
                    key=names[j]
                    if key=='realresult' or key=='result':
                        if value[key]!="":
                            strValue=str(value[key])
                            sheet.write(i,j,strValue)

                    #指定写入的格式，保留样式3
                    if cell:
                            ncell=_getCell(sheet,i,j)
                            if ncell:
                                    #设置写入后的格式和写入前一样
                                    ncell.xf_idx=cell.xf_idx
                   
        #保存文件       
        wb.save(df)
        print ("write finished")


    #复制表格
    def copy_open(self,srcfile,desfile):
        
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
        #print(workbook.sheet_names())
        
        sheet=wb.get_sheet("Sheet1")
        return  wb
    
        #wb.save(desfile)


       
if __name__ == "__main__":
    pass
    srcfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\debug\autoTestApi_demo\datadir\myHttp.xls"

    ex= ExcelUtil(srcfile)
    ex.dict_data()
	
 
