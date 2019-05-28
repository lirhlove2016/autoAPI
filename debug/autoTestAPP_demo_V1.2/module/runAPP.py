# coding:utf-8
from common import elementApp as app
from common import readexcel as reader, writeexcel as writer

import os

# -文件目录配置----------------------------
filepath = os.path.abspath(os.getcwd())
srcfile = os.path.join(filepath, 'datadir/myApp.xls')
desfile = os.path.join(filepath, 'datadir/myApp_result.xls')
resultfile = os.path.join(filepath, 'report/screenshot/screenshot_')
print(srcfile)

"""重构ing....."""


# -脚本-----------------------------------
def run(line):
    app.go_func(line[3],line[4], line[5],line[6], line[2])

reader.open_excel(srcfile)
writer.copy_open(srcfile, desfile)

for i in range(0, reader.r):
    line = reader.readline()
    print(line)
    if len(line[0]) >=2 or len(line[1])>=2 or line[0]=="#":
        # 不去执行的行
        pass
    else:
        # 执行
        run(line)
writer.save_close()

print('执行完成---------------')

# ----end------------------------------------------
