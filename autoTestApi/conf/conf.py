#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
version=1.0

'''
1.datafile
2.timeout
'''

#设置目录
filepath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dataDir=os.path.join(filepath,'datadir')
reportDir=os.path.join(filepath,'report')
resultDir=os.path.join(filepath,'result')
#timeout
TIMEOUT=10

#domain
API_ENV_ON=False #切换环境用,false,使用数据表
API_ENV_NOW="ceshi"

API_ENV={
    "ceshi":"ceshi.ishugui.cn",
    "api":"",
}


if __name__=="__main__":
    print(dataDir)
    print(reportDir)
    
