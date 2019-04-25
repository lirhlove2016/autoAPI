# coding:utf-8
from common import elementApp as app
from common import readexcel as reader, writeexcel as writer
from common import toast as t

import unittest
import time
import os
from  conf.conf import reportDir,htmlDir
from common import HTMLTestRunner

# -文件目录配置----------------------------
filepath = os.path.abspath(os.getcwd())
srcfile = os.path.join(filepath, 'datadir/myApp.xls')
desfile = os.path.join(filepath, 'datadir/myApp_result.xls')
resultfile = os.path.join(filepath, 'report/screenshot/screenshot_')
print(srcfile)

class testAPP(unittest.TestCase):
    def test_run(self):
        # -脚本-----------------------------------
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
                app.RIGHT()
                return
            if line[3] == 'left':
                app.LEFT()
                return
            if line[3] == 'up':
                app.UP()
                return
            if line[3] == 'down':
                app.DOWN()
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

            if line[3] == 'assertequals':
                #app.assert_equals(line[4], line[5],line[6])
                app.assert_method("equal",line[4], line[5],line[6])
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
                app.get_pagessource(line[4])
                return
            if line[3] == 'assertequals_all':
                app.assert_equals_all(line[4], line[5],line[6])
                return

            if line[3] == 'assertin':
                #app.assert_in(line[4], line[5],line[6])
                app.assert_method("in",line[4], line[5],line[6])
                return
            if line[3] == 'assertin_all':
                app.assert_in_all(line[4], line[5],line[6])
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
                app.xpath_exist(line[4],line[5])
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
        #writer.writeformula()
        writer.save_close()

        print('执行完成---------------')

    # ----end------------------------------------------


                
    
if __name__=="__main__":

    suite = unittest.TestSuite()
    suite.addTest(testAPP('test_run'))
    now = time.strftime("%Y-%m-%d %M-%H_%M_%S", time.localtime(time.time()))           
    htmlreport = htmlDir+r"/"+now+"_result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")

    runner.run(suite)
    fp.close()

    

    
    
