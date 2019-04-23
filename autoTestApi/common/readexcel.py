# coding:utf-8
import xlrd

workbook=None
sheet=None
rr=0  #逐行读取时的行数
r=0 #多少行

#逐行读取
def open_excel(srcfile):
    global workbook,sheet,r,rr
    #
    xlrd.Book.encoding='utf8'
    workbook=xlrd.open_workbook(filename=srcfile)
    #选取第一个工作表
    
    sheet=workbook.sheet_by_index(1)
    #设置r为当前sheet有多少行
    r=sheet.nrows
    rr=0
    return

'''
#逐行读取
def open_excel(srcfile):
    global workbook,sheet,r,rr
    #
    xlrd.Book.encoding='utf8'
    workbook=xlrd.open_workbook(filename=srcfile)
    #选取第一个工作表
    
    sheet=workbook.sheet_by_index(0)
    #设置r为当前sheet有多少行
    r=sheet.nrows
    rr=0
    return
'''

#逐行读取
def readline():
    global sheet,rr,r
    row=None

    #如果当前读取的行没有到最后一行，就去读一行
    if (rr<r):
        row=sheet.row_values(rr)
        rr=rr+1
    return row

        
if __name__ == "__main__":
   filename="D:\\workdtation\\mygitwork\\project\\autoTestApi\\myHttpdata.xlsx"
   open_excel(filename)
   #循环读取excel中所有内容，并打印出来
   for i in range(0,r):
       print(readline())
