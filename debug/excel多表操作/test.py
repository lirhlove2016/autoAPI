# coding:utf-8
import readexcel as reader
import writeexcel as writer
import os

# -文件目录配置----------------------------
filepath = os.path.abspath(os.getcwd())
srcfile = r'myapp_Http.xls'
desfile = r'myapp_xigua_result.xls'
print(srcfile,desfile)

ls=reader.open_excel(srcfile)
writer.copy_open(srcfile, desfile)

#读取多个sheet
print('len(ls)',len(ls))
for j in range(0,len(ls)):
    row=ls[j]
    for i in range(0,len(row)):
        line=row[i]              
        print("line %d is %s "%(i+1,line))            
        if len(line[0]) >=2 or len(line[1])>=2 or line[0]=="#":
            # 不去执行的行
            pass
        else:

            # 执行
            #run(line)
            print(reader.rr)
            print('正在写入第%d'%i)
            writer.write(i, 7, "fail")
            pass
         
#writer.write(reader.rr - 1, 7, result)
writer.save_close()

print('执行完成---------------')

# ----end------------------------------------------

