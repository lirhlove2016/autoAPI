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


    def write_excel(self,filepath,datas,names):
        """写入数据"""
        f = xlwt.Workbook(encoding='utf-8', style_compression=0)             
        sheet= f.add_sheet(u'sheet1',cell_overwrite_ok=True) 




       
        #写入数据
        d=[]
        for i in range(len(datas)):
            value=datas[i]
            #print("正在写入第{0}行，数据{1}".format(i+1,value)) 
            for j in range(len(names)):

               #获取要写入的单元格
                def _getCell(sheet,r,c):
                        #获取行
                        row=sheet._Worksheet__rows.get(i)
                        if not row:
                                return None
                        #获取单元格
                        cell=row._Row__cells.get(j)
                        return cell

                #获取要写入的单元格
                cell=_getCell(sheet,i,j)

                #
                key=names[j]
                if key=='执行状态':
                    strValue=str(value[key])
                    sheet.write(i+1,j,strValue) 

                #指定写入的格式
                if cell:
                        ncell=_getCell(sheet,i,j)
                        if ncell:
                                #设置写入后的格式和写入前一样
                                ncell.xf_idx=cell.xf_idx


                    
               
        f.save(filepath)
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
        wb.save(desfile)


       
if __name__ == "__main__":
    pass
    srcfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\debug\autoTestApi_demo\datadir\myHttp.xls"

    ex= ExcelUtil(srcfile)
    ex.dict_data()
	
 
