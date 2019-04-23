'''
import unittest,time,os
from BeautifulReport import BeautifulReport

import login_manager

current_path = os.getcwd()
report_path = os.path.join(current_path, "Report")
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
# 报告地址&名称
report_title = 'Example报告' + now + ".html"  # 如果不能打开这个文件，可能是now的格式，不支持：和空格

if __name__ == '__main__':
    suite = unittest.TestSuite()  
    loader=unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(login_manager))
    #运行用例filename=报告名称，description=所有用例总的名称，log_path=报告路径,如果不填写默认当前目录
    BeautifulReport(suite).report(filename="测试报告", description ='login_manager模块', log_path =report_path)

'''
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader.discover(".",pattern="logn*.py",top_level_dir=None)     #"."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='百度测试报告', description='搜索测试', log_path='.')    #log_path='.'把report放到当前目录下
