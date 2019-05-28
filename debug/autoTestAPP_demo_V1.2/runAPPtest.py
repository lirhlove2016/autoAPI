# coding:utf-8
from common import elementApp as app
from common import readexcel as reader, writeexcel as writer
from common import toast as t
import os
import time
import datetime
# -文件目录配置----------------------------
filepath = os.path.abspath(os.getcwd())
srcfile = os.path.join(filepath, 'datadir/myApp.xls')
desfile = os.path.join(filepath, 'datadir/myApp_result.xls')
resultfile = os.path.join(filepath, 'report/screenshot/screenshot_')
print(srcfile)

# -脚本-----------------------------------
#时间
start_time=datetime.datetime.now()
#执行
def run(line):
    if line[3] == 'caps':
        app.update_capability(line[4], line[5])
        return
    if line[3] == 'start':
        print(app.desired_caps)
        app.start(line[4], line[5])
        return
    if line[3] == 'sleep':
        app.sleep(line[4])
        return
    if line[3] == 'right':
        app.swiptest("right",line[4])
        return
    if line[3] == 'left':
        app.swiptest("left",line[4])
        return
    if line[3] == 'up':
        app.swiptest("up", line[4])
        return
    if line[3] == 'down':
        app.swiptest("down", line[4])
        return
    if line[3] == 'id':
        app.get_element("id", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'name':
        app.get_element("name", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'text':
        app.get_element("text", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'css':
        app.get_element("css", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'xpath':
        app.get_element("xpath", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'class':
        app.get_element("class", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'click':
        app.clicks("click", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'clear':
        app.clicks("clear", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'input':
        app.clicks("input", line[4], line[5], line[6], line[2])

        return
    if line[3] == 'savephoto':
        app.get_screenshot(resultfile, line[4])
        return
    if line[3] == 'text':
        app.get_element("text", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'quit':
        app.quit()
        return
    if line[3] == 'back':
        app.back()
        return
    if line[3]=='pagesource':
        app.get_pagesource(line[4])
        return
    if line[3] == 'assertequal':
        app.assert_method("equal",line[4], line[5],line[6])
        return
    if line[3] == 'assertin':
        app.assert_method("in",line[4], line[5],line[6])
        return
    if line[3] == 'assertnotequal':
        app.assert_method("notequal",line[4], line[5],line[6])
        return
    if line[3] == 'assertnotin':
        app.assert_method("notin",line[4], line[5],line[6])
        return
    if line[3] == 'assert_all_e':
        app.assert_all_method("equal",line[4], line[5],line[6])
        return
    if line[3] == 'assert_all_in':
        app.assert_all_method("in", line[4], line[5], line[6])
        return
    if line[3] == 'assertin_allnot_e':
        app.assert_all_method("notequal", line[4], line[5], line[6])
        return
    if line[3] == 'assertin_allnot_in':
        app.assert_all_method("notin", line[4], line[5], line[6])
        return
    if line[3] == 'toast':
        t.is_toast_exists(app.driver,line[4],line[5],line[6])
        return
    if line[3] == 'alwaysallow':
        t.always_allow(app.driver,line[4])
        return    

    if line[3] == 'textContains':
        app.get_element("textContains", line[4], line[5], line[6], line[2])
        return
    if line[3] == 'isexist':
        app.is_exist(line[4],line[5])
        return
    
    if line[3] == 'tanchuang':
        app.tanchuang(line[4])
        return
    if line[3] == 'tanchuangall':
        app.tanchuang_all()
        return   
    if line[3] == 'backs':
        app.backs(line[4])
        return

    if line[3]=='tappoint':
        app.tap_point(line[4],line[5])
        return
    
    if line[3]=='taprandom':
        app.tap_random()
        return
            
    if line[3]=='pagesource':
        app.get_pagessource(line[4])
        return

    if line[3]=='sourceassert':
        app.source_assert(line[4])
        return

    if line[3]=='activity':
        app.get_current_activity()
        return
    if line[3]=='get_velue':
        app.get_value(line[4],line[5])
        return
    if line[3]=='const_int':
        app.const_value("int",line[4],line[5])

        return
    if line[3]=='const':
        app.const_value("",line[4],line[5])
        return

    else:
        print('没有这个方法，请检查',line[3])

        return

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

#写入公式
app.write_formula()
#保存
writer.save_close()
#时间
end_time=datetime.datetime.now()
v=end_time-start_time
print("运行时间:%s s"%(v.days*24*3600+v.seconds))
print('执行完成---------------')
# ----end------------------------------------------
