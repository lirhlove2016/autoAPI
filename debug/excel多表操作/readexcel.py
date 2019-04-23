# coding:utf-8
import xlrd

'''
实现功能:
1.逐行读取sheet
2.读取多个sheet表

'''
#工作表数
workbook=None
sheet=None
rr=0  #逐行读取时的行数
r=0 #多少行


#逐行读取
def open_excel(srcfile):
    global workbook,sheet,r,rr
    xlrd.Book.encoding='utf8'
    workbook=xlrd.open_workbook(filename=srcfile)
    #多个表
    rsheets=[]
    rlines=[]
    
    # 获取workbook中所有的表格
    sheets = workbook.sheet_names()    
    for i in range(len(sheets)):
        sheet=workbook.sheet_by_index(i)
        print("当前是read第%d表%s"%(i+1,sheets[i]))      
        r=sheet.nrows
        rr=0
        print('共 %s 行'%r)
        
        #当前表的所有行
        ls=[]
        for i in range(0, r):
            line = readline()           
            #print(line)
            #print("line %d is %s "%(i+1,line))
            
            ls.append(line)            
        rlines.append(ls)                    
    return rlines

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
   pass
