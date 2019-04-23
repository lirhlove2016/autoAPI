# coding:utf-8
import json
import unittest
import time
import os

from common import HTMLTestRunner
from  app_runall  import testAPI
from conf.conf import *
    
if __name__=="__main__":
    #unittest.main()
    print(dataDir,reportDir)
    
    suite = unittest.TestSuite()
    suite.addTest(testAPI('test_app_api'))

    now = time.strftime("%Y-%m-%d %M-%H_%M_%S", time.localtime(time.time()))           
    htmlreport = reportDir+r"/"+now+"_result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")

    runner.run(suite)
    fp.close()

    

    
    
