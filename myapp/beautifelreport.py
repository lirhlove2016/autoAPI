import unittest
from BeautifulReport import BeautifulReport    #导入BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader.discover(".",pattern="*tests.py",top_level_dir=None)     #"."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='百度测试报告', description='搜索测试', log_path='.')    #log_path='.'把report放到当前目录下