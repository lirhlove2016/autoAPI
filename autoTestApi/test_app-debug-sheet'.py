# coding:utf-8
from common import Http
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
import re

import xlrd,xlwt

srcfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\autoTestApi\123.xls"
desfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\autoTestApi\myHttp333_result.xls"


def writerme(path):
    wb=xlwt.Workbook()
    
    sheet=wb.add_sheet("sheet1")
    value = [["名称", "价格", "出版社", "语言"], ["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"], ["暗时间", "32.4", "人民邮电出版社", "中文"], ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]

    for i in range(0,4):
        for j in range(0,len(value[i])):
            sheet.write(i,j,value[i][j])
    wb.save(path)
    print('write')

def readerme(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    for i in range(0,worksheet.nrows):
        row=worksheet.row(i)
        for j in range(0,worksheet.ncols):
            print(worksheet.cell_value(i,j),"\t", end="")
        print()    
    
readerme(srcfile)
writerme(srcfile)


        

'''

def run(line):
    if line[3]=='post':
        Http.api_request('post',line[4],line[5])
        return
    if line[3]=='get':
        Http.api_request('get',line[4],line[5])
        return
    if line[3]=='put':
        Http.api_request('put',line[4],line[5])
        return

    if line[3]=='addheader':
        Http.add_header(line[4],line[5])
        return
    if line[3]=='assertequals':
        Http.assert_equals(line[4],line[5])
        return
    if line[3]=='savejson':
        Http.saveJson(line[4],line[5])
        return
    if  line[3]=='seturl':
        Http.seturl(line[4])
        return
    if  line[3]=='settimeout':
        Http.settimeout(line[4])
        return
    if  line[3]=='addparam':
        Http.add_param(line[4],line[5])
        return
    if  line[3]=='removeheader':
        Http.remove_header(line[4])
        return
        

reader.open_excel(srcfile)
writer.copy_open(srcfile,desfile)

for i in range(0,reader.r):
	line=reader.readline()
	print(line)
	if len(line[0])>2 or len(line[1])>2:
		#不去执行的行
		pass
	else:
		#执行
		run(line)
		pass
														
writer.save_close()
'''
